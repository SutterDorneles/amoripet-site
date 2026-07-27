from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "produtos_novos"
OUT = BASE / "produtos_prontos"
OUT.mkdir(exist_ok=True)

catalog = [
    {
        "key": "caminha-zimbapet-damask",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.29.29.jpeg",
        "nome": "Caminha ZimbaPet Damask e Poá",
        "descricao": "Caminha premium com laterais em poá, almofada removível em estampa damask, laço decorativo e acabamento em cordão. Conforto e estilo para cães e gatos.",
        "categoria": "acessorios",
        "preco": "359.80",
    },
    {
        "key": "toca-vaquinha-plush",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.29.29 (2).jpeg",
        "nome": "Toca Caminha Vaquinha Plush",
        "descricao": "Toca iglu em pelúcia com estampa de vaquinha, chifres, orelhas e abertura acolchoada. Aconchego para cães e gatos de pequeno porte.",
        "categoria": "acessorios",
        "preco": "304.90",
    },
    {
        "key": "toca-ridell-ursinhos",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.29.30.jpeg",
        "nome": "Toca Ridell Pet Premium Ursinhos",
        "descricao": "Toca iglu Ridell em pelúcia azul com estampa de ursinhos, estrelas e nuvens. Acabamento com pompons e almofada removível.",
        "categoria": "acessorios",
        "preco": "305.90",
    },
    {
        "key": "caminha-ridelf-sage-cordao",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.32.59.jpeg",
        "nome": "Caminha Ridelf Pet Premium Verde Sage",
        "descricao": "Caminha retangular com laterais acolchoadas, tecido texturizado verde sage e acabamento em cordão creme. Almofada central confortável.",
        "categoria": "acessorios",
        "preco": "133.90",
    },
    {
        "key": "caminha-ridelf-cinza-cordao",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.33.23.jpeg",
        "nome": "Caminha Ridelf Pet Premium Cinza",
        "descricao": "Caminha retangular premium em tecido cinza texturizado, laterais altas e cordão decorativo. Almofada central espessa e confortável.",
        "categoria": "acessorios",
        "preco": "251.90",
    },
    {
        "key": "leevre-grande-porte",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.42.02.jpeg",
        "nome": "Leevre Coleira Cães Grande Porte — Ourofino",
        "descricao": "Coleira antiparasitária super premium com deltametrina e propoxur. Proteção contra carrapatos (até 6 meses), pulgas (até 9 meses) e flebótomo/leishmaniose (até 6 meses). 63 cm.",
        "categoria": "farmacia",
        "preco": "189.35",
    },
    {
        "key": "leevre-pequeno-medio",
        "arquivo": "WhatsApp Image 2026-07-21 at 15.46.31.jpeg",
        "nome": "Leevre Coleira Cães Pequeno e Médio Porte — Ourofino",
        "descricao": "Coleira antiparasitária com deltametrina e propoxur. Carrapatos até 6 meses, pulgas até 9 meses e flebótomo até 6 meses. 48 cm.",
        "categoria": "farmacia",
        "preco": "177.60",
    },
    {
        "key": "auritop-15g",
        "arquivo": "WhatsApp Image 2026-07-21 at 16.04.16.jpeg",
        "nome": "Auritop Gel Otológico 15g — Ourofino",
        "descricao": "Gel otológico anti-inflamatório, analgésico, antibacteriano e antimicótico. Indicado para otites externas e cães atópicos. Uso veterinário para cães e gatos.",
        "categoria": "farmacia",
        "preco": "86.90",
    },
    {
        "key": "prednisolona-paraquenos-10",
        "arquivo": "WhatsApp Image 2026-07-21 at 16.05.08.jpeg",
        "nome": "Antiinflamatório Prednisolona Paraquenos — 10 comprimidos",
        "descricao": "Corticóide oral anti-inflamatório e antialérgico de uso veterinário. 1 blister com 10 comprimidos sulcados em 4. Para cães e gatos.",
        "categoria": "farmacia",
        "preco": "26.90",
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

out_json = BASE / "petshop" / "catalogo_lote3.json"
out_json.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print("TOTAL", len(catalog))
print("JSON", out_json)
