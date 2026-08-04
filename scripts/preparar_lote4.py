from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "produtos_novos"
OUT = BASE / "produtos_prontos"
OUT.mkdir(exist_ok=True)

catalog = [
    {
        "key": "premier-nattu-bites-frango",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.13.jpeg",
        "nome": "PremieR Nattu Bites Frango e Superfoods",
        "descricao": "Biscoito Super Premium para cães de todos os portes e idades. Frango, batata-doce, brócolis, cenoura e cranberry. Sem corantes e aromatizantes artificiais.",
        "categoria": "petiscos",
        "preco": "9.50",
    },
    {
        "key": "hana-dental-care-60",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.13 (1).jpeg",
        "nome": "Hana Healthy Life Dental Care Mini e Pequenas 60g",
        "descricao": "Petisco para cuidado oral de raças mini e pequenas. Ideal para auxiliar na limpeza dos dentes e reduzir a formação de tártaro.",
        "categoria": "petiscos",
        "preco": "13.60",
    },
    {
        "key": "hana-sensitive-65",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.13 (2).jpeg",
        "nome": "Hana Healthy Life Sensitive Salmão 65g",
        "descricao": "Alimento específico para cães adultos. Proteína de salmão com ômega 3 e 6 — ideal para cães alérgicos e saúde da pele.",
        "categoria": "petiscos",
        "preco": "13.60",
    },
    {
        "key": "hana-dogzen-100",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.13 (3).jpeg",
        "nome": "Hana Healthy Life DogZen 100g",
        "descricao": "Alimento específico para cães adultos agitados. Camomila, valeriana, L-triptofano e prebióticos — calmantes naturais.",
        "categoria": "petiscos",
        "preco": "13.60",
    },
    {
        "key": "hana-vitajoint-100",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.14.jpeg",
        "nome": "Hana Healthy Life VitaJoint 100g",
        "descricao": "Alimento específico para cães adultos e idosos. Condroitina, glicosamina e prebióticos — auxilia na saúde dos ossos e articulações.",
        "categoria": "petiscos",
        "preco": "13.60",
    },
    {
        "key": "formula-natural-fresh-meat-25kg",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.36.jpeg",
        "nome": "Fórmula Natural Fresh Meat Adultos Mini e Pequeno 2,5kg",
        "descricao": "Ração Super Premium Grain Free com carne de frango, mandioca e alecrim. Equilíbrio da microbiota, pelagem brilhante e antioxidantes naturais.",
        "categoria": "racoes",
        "preco": "103.90",
    },
]

SIZE = 1000


def prepare(src_path: Path, dest_path: Path) -> None:
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = max(0, (h - side) // 2 - int(side * 0.05))
    img = img.crop((left, top, left + side, top + side))
    img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    img.save(dest_path, "JPEG", quality=88, optimize=True)


for item in catalog:
    src = SRC / item["arquivo"]
    if not src.exists():
        raise SystemExit(f"Faltando: {src}")
    dest_name = f"{item['key']}.jpg"
    prepare(src, OUT / dest_name)
    item["imagem"] = dest_name
    print("OK", dest_name, item["preco"])

out_json = BASE / "petshop" / "catalogo_lote4.json"
out_json.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print("TOTAL", len(catalog))
print("JSON", out_json)
