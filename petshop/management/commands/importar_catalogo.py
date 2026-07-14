import json
import shutil
from decimal import Decimal
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from petshop.models import Categoria, Produto


class Command(BaseCommand):
    help = "Importa o catálogo de produtos do lote (JSON + imagens em produtos_prontos)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limpar-placeholders",
            action="store_true",
            help="Remove produtos antigos sem imagem real do lote",
        )

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parents[3]
        json_path = base_dir / "petshop" / "catalogo_lote1.json"
        imagens_dir = base_dir / "produtos_prontos"

        if not json_path.exists():
            self.stderr.write(self.style.ERROR(f"Arquivo não encontrado: {json_path}"))
            return

        catalog = json.loads(json_path.read_text(encoding="utf-8"))

        nomes_mapa = {
            "farmacia": "Farmácia",
            "higiene": "Higiene",
            "acessorios": "Acessórios",
            "petiscos": "Petiscos",
            "racoes": "Rações",
        }

        if options["limpar_placeholders"]:
            keys = {item["key"] for item in catalog}
            removidos = 0
            for produto in Produto.objects.all():
                nome_arquivo = Path(produto.imagem.name).stem if produto.imagem else ""
                if nome_arquivo in keys:
                    continue
                # mantém só itens do lote novo; remove placeholders
                produto.delete()
                removidos += 1
            self.stdout.write(self.style.WARNING(f"Placeholders removidos: {removidos}"))

        criados = 0
        atualizados = 0

        for item in catalog:
            cat_slug = item["categoria"]
            categoria, _ = Categoria.objects.get_or_create(
                slug=cat_slug,
                defaults={"nome": nomes_mapa.get(cat_slug, cat_slug.title())},
            )
            if categoria.nome != nomes_mapa.get(cat_slug, categoria.nome):
                categoria.nome = nomes_mapa.get(cat_slug, categoria.nome)
                categoria.save()

            produto, created = Produto.objects.get_or_create(
                nome=item["nome"],
                defaults={
                    "categoria": categoria,
                    "descricao": item.get("descricao", ""),
                    "preco": Decimal(item["preco"]),
                    "disponivel": True,
                    "destaque": True,
                    "estoque": 10,
                },
            )

            produto.categoria = categoria
            produto.descricao = item.get("descricao", "")
            produto.preco = Decimal(item["preco"])
            produto.preco_promocional = None
            produto.disponivel = True
            produto.destaque = True
            produto.selo_oferta = False
            produto.estoque = 10

            imagem_src = imagens_dir / item["imagem"]
            if imagem_src.exists():
                destino_rel = f"produtos/{item['imagem']}"
                destino_abs = base_dir / "media" / destino_rel
                destino_abs.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(imagem_src, destino_abs)
                with open(destino_abs, "rb") as fh:
                    produto.imagem.save(item["imagem"], File(fh), save=False)

            produto.save()
            if created:
                criados += 1
                self.stdout.write(self.style.SUCCESS(f"+ {produto.nome}"))
            else:
                atualizados += 1
                self.stdout.write(f"~ {produto.nome}")

        self.stdout.write(
            self.style.SUCCESS(
                f"Pronto: {criados} criados, {atualizados} atualizados. Total no lote: {len(catalog)}"
            )
        )
