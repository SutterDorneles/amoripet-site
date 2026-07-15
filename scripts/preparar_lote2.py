from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "produtos_novos"
OUT = BASE / "produtos_prontos"
OUT.mkdir(exist_ok=True)

catalog = [
    {
        "key": "omega-top-3-40",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.16.39.jpeg",
        "nome": "Omega Top 3 EPA + DHA 500mg — 40 cápsulas",
        "descricao": "Suplemento alimentar Agener União com ômega 3 para cães e gatos. 40 cápsulas moles saborosas.",
        "categoria": "farmacia",
        "preco": "86.50",
    },
    {
        "key": "qpelo-pet-40",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.17.14.jpeg",
        "nome": "QPelo Pet Biotina e Cistina — 40 comprimidos",
        "descricao": "Suplemento Agener União para pelos fortes e brilhantes. Biotina, cistina e extrato de leveduras.",
        "categoria": "farmacia",
        "preco": "107.90",
    },
    {
        "key": "procart-flex-40",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.18.06.jpeg",
        "nome": "PRO cart FLEX Colágeno UC-II — 40 cápsulas",
        "descricao": "Suplemento articular com colágeno UC-II patenteado, zero açúcar. 40 cápsulas moles saborosas.",
        "categoria": "farmacia",
        "preco": "281.90",
    },
    {
        "key": "glicol-pet-120",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.19.48.jpeg",
        "nome": "Organnact Glicol Pet 120ml",
        "descricao": "Energético e estímulo do apetite com glicose, vitaminas e aminoácidos. Para cães, gatos e outros pets.",
        "categoria": "farmacia",
        "preco": "79.90",
    },
    {
        "key": "glicovet-gold-120",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.20.24.jpeg",
        "nome": "Glicovet Gold 120ml",
        "descricao": "Suplemento vitamínico, mineral e de aminoácidos VetBras. Minerais quelatados, taurina e glutamina.",
        "categoria": "farmacia",
        "preco": "38.90",
    },
    {
        "key": "dental-guard-85",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.24.01.jpeg",
        "nome": "Soft Care Dental Guard 85g",
        "descricao": "Gel dental de suave abrasão. Previne cálculo, elimina mau hálito. Sem flúor e sem açúcar.",
        "categoria": "higiene",
        "preco": "41.90",
    },
    {
        "key": "dental-special-care-40",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.24.51.jpeg",
        "nome": "Soft Care Dental Special Care 40g",
        "descricao": "Gel odontológico com própolis e ácido hialurônico para dentes e gengivas sensíveis. Sem álcool e açúcar.",
        "categoria": "higiene",
        "preco": "41.90",
    },
    {
        "key": "eye-clean-up-100",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.25.33.jpeg",
        "nome": "Soft Care Eye Clean Up 100ml",
        "descricao": "Higiene da face, ao redor dos olhos e focinho. Remove crostas e odores. pH balanceado.",
        "categoria": "higiene",
        "preco": "49.90",
    },
    {
        "key": "stress-away-100",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.27.18.jpeg",
        "nome": "Soft Care Stress Away 100ml",
        "descricao": "Linha bem-estar com óleos essenciais de capim-limão, lavanda e camomila. Bem-estar e conforto.",
        "categoria": "higiene",
        "preco": "76.90",
    },
    {
        "key": "pet-serenity-spray-100",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.28.44.jpeg",
        "nome": "Soft Care Pet Serenity Spray 100ml",
        "descricao": "Spray de bem-estar com óleos essenciais de lavanda, ylang-ylang e valeriana.",
        "categoria": "higiene",
        "preco": "83.90",
    },
    {
        "key": "premier-cookie-adultos-250",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.29.42.jpeg",
        "nome": "PremieR Cookie Adultos Sabor Original 250g",
        "descricao": "Cookies assados, crocantes e nutritivos. Saúde oral, zinco, biotina e prebiótico.",
        "categoria": "petiscos",
        "preco": "18.90",
    },
    {
        "key": "premier-yorkshire-25kg",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.30.10.jpeg",
        "nome": "PremieR Raças Específicas Yorkshire Adultos 2,5kg",
        "descricao": "Ração Super Premium sabor frango para Yorkshire adultos a partir de 12 meses.",
        "categoria": "racoes",
        "preco": "105.00",
    },
    {
        "key": "premier-ambientes-internos-1kg",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.30.33.jpeg",
        "nome": "PremieR Ambientes Internos Adultos 1kg",
        "descricao": "Ração Super Premium frango e salmão para cães de porte pequeno adultos (1 a 7 anos).",
        "categoria": "racoes",
        "preco": "46.95",
    },
    {
        "key": "premier-shih-tzu-25kg",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.37.19.jpeg",
        "nome": "PremieR Raças Específicas Shih Tzu Adultos 2,5kg",
        "descricao": "Ração Super Premium sabor frango para Shih Tzu adultos a partir de 12 meses.",
        "categoria": "racoes",
        "preco": "104.90",
    },
    {
        "key": "bom-amigo-pescinip",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.38.26.jpeg",
        "nome": "Bom Amigo Pescinip — Brinquedo com Catnip",
        "descricao": "Brinquedo para gatos em formato de peixe com catnip.",
        "categoria": "acessorios",
        "preco": "15.90",
    },
    {
        "key": "bom-amigo-pic-pockynip",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.40.36.jpeg",
        "nome": "Bom Amigo Pic Pockynip — Palitos Catnip",
        "descricao": "Brinquedo para gatos com palitos de catnip/matatabi.",
        "categoria": "acessorios",
        "preco": "30.20",
    },
    {
        "key": "bom-amigo-happynip",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.41.20.jpeg",
        "nome": "Bom Amigo Happynip — Brinquedo com Catnip",
        "descricao": "Brinquedo para gatos com catnip e pena.",
        "categoria": "acessorios",
        "preco": "15.20",
    },
    {
        "key": "mytex-arraia",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.44.22.jpeg",
        "nome": "My Tex Toys Brinquedo Arraia para Gatos",
        "descricao": "Brinquedo soft toys: distrai, diverte e alivia o estresse. Não machuca gengivas.",
        "categoria": "acessorios",
        "preco": "32.90",
    },
    {
        "key": "mytex-peixe",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.45.30.jpeg",
        "nome": "My Tex Toys Brinquedo Peixe para Gatos",
        "descricao": "Brinquedo soft toys colorido. Distrai, diverte e alivia o estresse.",
        "categoria": "acessorios",
        "preco": "32.99",
    },
    {
        "key": "mytex-galinha",
        "arquivo": "WhatsApp Image 2026-07-14 at 14.47.02.jpeg",
        "nome": "My Tex Toys Brinquedo Galinha para Gatos",
        "descricao": "Brinquedo soft toys em formato de galinha. Ajuda a aliviar o estresse e a solidão.",
        "categoria": "acessorios",
        "preco": "41.90",
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

out_json = BASE / "petshop" / "catalogo_lote2.json"
out_json.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print("TOTAL", len(catalog))
print("JSON", out_json)
