from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "produtos_novos"
OUT = BASE / "produtos_prontos"
OUT.mkdir(exist_ok=True)

catalog = [
    {
        "key": "premier-nattu-adultos-pequeno-101kg",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.56.jpeg",
        "nome": "PremieR Nattu Adultos Porte Pequeno 10,1kg",
        "descricao": "Ração Super Premium com Super Foods: frango, abóbora, brócolis, quinoa e blueberry. Para cães adultos a partir de 12 meses, porte pequeno.",
        "categoria": "racoes",
        "preco": "288.65",
    },
    {
        "key": "golden-formula-adultos-pequeno-15kg",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.56 (1).jpeg",
        "nome": "GoldeN Formula Adultos Porte Pequeno 15kg",
        "descricao": "Ração sabor carne, arroz e vegetais para cães adultos de porte pequeno. Mini Bit, saúde oral, intestino saudável e pelagem sedosa.",
        "categoria": "racoes",
        "preco": "183.90",
    },
    {
        "key": "royal-canin-exigent-15kg",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.57.jpeg",
        "nome": "Royal Canin Exigent Gatos Adultos 1,5kg",
        "descricao": "Ração para gatos adultos com apetite muito exigente. Dupla sensação de sabor, peso ideal, sem corantes e aromatizantes artificiais.",
        "categoria": "racoes",
        "preco": "131.90",
    },
    {
        "key": "royal-canin-castrados-15kg",
        "arquivo": "WhatsApp Image 2026-07-29 at 15.23.57 (1).jpeg",
        "nome": "Royal Canin Castrados Sterilised 1,5kg",
        "descricao": "Ração para gatos adultos castrados. Controle de peso, alto teor de proteínas, sem corantes e aromatizantes artificiais.",
        "categoria": "racoes",
        "preco": "131.90",
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

out_json = BASE / "petshop" / "catalogo_lote5.json"
out_json.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print("TOTAL", len(catalog))
print("JSON", out_json)
