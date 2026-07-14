from pathlib import Path
import json
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "produtos_novos"
OUT = BASE / "produtos_prontos"
OUT.mkdir(exist_ok=True)

catalog = [
    {
        "key": "scalibor-pequeno-medio",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.22.27.jpeg",
        "nome": "Scalibor Coleira Antiparasitária Pequeno/Médio",
        "descricao": "Coleira antiparasitária à base de deltametrina para cães pequenos e médios. Auxilia no controle de flebotomíneos, moscas, pulgas e carrapatos.",
        "categoria": "farmacia",
        "preco": "90.90",
    },
    {
        "key": "cloresten-500",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.26.04.jpeg",
        "nome": "Cloresten Xampu Antifúngico e Antibacteriano 500ml",
        "descricao": "Xampu veterinário Agener Derma com queratina hidrolisada. Antifúngico e antibacteriano para cães e gatos.",
        "categoria": "higiene",
        "preco": "207.90",
    },
    {
        "key": "k-treat-cond-290",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.30.01.jpeg",
        "nome": "Soft Care K-Treat Condicionador Micelar 290ml",
        "descricao": "Condicionador micelar enriquecido com fitoesfingosina e proteína de baobá. Ideal para pele sensível.",
        "categoria": "higiene",
        "preco": "145.00",
    },
    {
        "key": "k-treat-shampoo-500",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.34.11.jpeg",
        "nome": "Soft Care K-Treat Shampoo Micelar 500ml",
        "descricao": "Shampoo micelar sulfate free, sem parabenos, com fitoesfingosina e proteína de baobá.",
        "categoria": "higiene",
        "preco": "180.00",
    },
    {
        "key": "k-treat-shampoo-300",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.35.00.jpeg",
        "nome": "Soft Care K-Treat Shampoo Micelar 300ml",
        "descricao": "Shampoo micelar Soft Care Linha Dermato. Sulfate free, sem parabenos, pH balanceado.",
        "categoria": "higiene",
        "preco": "139.90",
    },
    {
        "key": "propcalm-300",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.35.49.jpeg",
        "nome": "Soft Care Propcalm Shampoo 300ml",
        "descricao": "Shampoo enriquecido com própolis, tensoativos extra suaves. Hidratação e proteção à pele e pelagem.",
        "categoria": "higiene",
        "preco": "125.90",
    },
    {
        "key": "primer-pre-shampoo-300",
        "arquivo": "WhatsApp Image 2026-07-06 at 10.37.28.jpeg",
        "nome": "Soft Care Primer Pré-Shampoo 300ml",
        "descricao": "Pré-shampoo enriquecido com camomila. Ideal para pele sensível e pelagem ressecada.",
        "categoria": "higiene",
        "preco": "80.90",
    },
    {
        "key": "zelotril-oto-30",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.20.35.jpeg",
        "nome": "Zelotril Oto Emulsão Otológica 30ml",
        "descricao": "Emulsão otológica antibacteriana, antimicótica e anti-inflamatória para cães. Agener União.",
        "categoria": "farmacia",
        "preco": "108.90",
    },
    {
        "key": "bebedouro-ideal-dog",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.21.01.jpeg",
        "nome": "Bebedouro Automático Ideal Dog Anti Bactéria",
        "descricao": "Bebedouro automático com proteção antibacteriana 99,9%. Ideal Dog.",
        "categoria": "acessorios",
        "preco": "124.90",
    },
    {
        "key": "carrinho-pet-vinho",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.22.23.jpeg",
        "nome": "Carrinho de Passeio para Pet - Vinho",
        "descricao": "Carrinho de passeio com capota de tela, cesto inferior e estrutura metálica. Cor vinho.",
        "categoria": "acessorios",
        "preco": "1090.00",
    },
    {
        "key": "carrinho-pet-azul",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.23.49.jpeg",
        "nome": "Carrinho de Passeio para Pet - Azul",
        "descricao": "Carrinho de passeio com capota, ventilação em tela e cesto inferior. Cor azul.",
        "categoria": "acessorios",
        "preco": "1090.00",
    },
    {
        "key": "wc-cat-new",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.24.20.jpeg",
        "nome": "Caixa de Areia Fechada WC Cat New",
        "descricao": "Caixa de areia fechada Plast Pet com porta, travas laterais e suporte para filtro de carvão.",
        "categoria": "higiene",
        "preco": "136.90",
    },
    {
        "key": "otomax-125",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.34.12.jpeg",
        "nome": "Otomax Uso Tópico 12,5g",
        "descricao": "Medicamento otológico veterinário MSD com sulfato de gentamicina, valerato de betametasona e clotrimazol.",
        "categoria": "farmacia",
        "preco": "100.90",
    },
    {
        "key": "hidrapet-creme-500",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.42.09.jpeg",
        "nome": "Hidrapet Creme Pós-Banho Sem Enxágue 500g",
        "descricao": "Creme pós-banho sem enxágue Agener Derma. Protege, hidrata e restaura a pelagem.",
        "categoria": "higiene",
        "preco": "237.70",
    },
    {
        "key": "hidrapet-xampu-200",
        "arquivo": "WhatsApp Image 2026-07-06 at 15.43.25.jpeg",
        "nome": "Hidrapet Xampu Hidratante 200ml",
        "descricao": "Xampu hidratante para cães e gatos. Protege, hidrata e restaura.",
        "categoria": "higiene",
        "preco": "126.90",
    },
    {
        "key": "bioflora-pet-tabs",
        "arquivo": "WhatsApp Image 2026-07-08 at 09.47.50.jpeg",
        "nome": "Soft Care Bioflora Pet Tabs 30 tabletes",
        "descricao": "Suplemento com probióticos, prebióticos e betaglucanos. 30 tabletes mastigáveis para cães e gatos.",
        "categoria": "farmacia",
        "preco": "129.90",
    },
    {
        "key": "serenity-pet-tabs",
        "arquivo": "WhatsApp Image 2026-07-08 at 09.50.12.jpeg",
        "nome": "Soft Care Serenity Pet Tabs 30 tabletes",
        "descricao": "Suplemento com triptofano e valeriana para controle do estresse. 30 tabletes mastigáveis.",
        "categoria": "farmacia",
        "preco": "146.90",
    },
    {
        "key": "immunity-pet-tabs",
        "arquivo": "WhatsApp Image 2026-07-08 at 09.52.22.jpeg",
        "nome": "Soft Care Immunity Pet Tabs 30 tabletes",
        "descricao": "Apoio nutricional com betaglucanos para idosos, filhotes e convalescentes. 30 tabletes mastigáveis.",
        "categoria": "farmacia",
        "preco": "129.90",
    },
    {
        "key": "hep-same-pet-tabs",
        "arquivo": "WhatsApp Image 2026-07-08 at 09.52.59.jpeg",
        "nome": "Soft Care HEP SAMe Pet Tabs 30 tabletes",
        "descricao": "Auxilia o metabolismo hepático com ação antioxidante. Contém SAMe e silimarina.",
        "categoria": "farmacia",
        "preco": "254.90",
    },
    {
        "key": "vitality-eye-mind",
        "arquivo": "WhatsApp Image 2026-07-08 at 09.54.40.jpeg",
        "nome": "Soft Care Vitality Eye & Mind 30 comprimidos",
        "descricao": "Suplemento para saúde de animais idosos. 1 comprimido para 5kg. 30 comprimidos palatáveis.",
        "categoria": "farmacia",
        "preco": "131.90",
    },
    {
        "key": "bravecto-2-45",
        "arquivo": "WhatsApp Image 2026-07-08 at 10.06.50.jpeg",
        "nome": "Bravecto Cães 2 a 4,5 kg",
        "descricao": "Comprimido mastigável contra carrapatos e pulgas. 12 semanas de proteção. 112,5 mg de fluralaner.",
        "categoria": "farmacia",
        "preco": "175.90",
    },
    {
        "key": "bravecto-45-10",
        "arquivo": "WhatsApp Image 2026-07-08 at 10.01.00.jpeg",
        "nome": "Bravecto Cães 4,5 a 10 kg",
        "descricao": "Comprimido mastigável contra carrapatos e pulgas. 12 semanas de proteção. 250 mg de fluralaner.",
        "categoria": "farmacia",
        "preco": "207.90",
    },
    {
        "key": "bravecto-10-20",
        "arquivo": "WhatsApp Image 2026-07-08 at 10.05.05.jpeg",
        "nome": "Bravecto Cães 10 a 20 kg",
        "descricao": "Comprimido mastigável contra carrapatos e pulgas. 12 semanas de proteção. 500 mg de fluralaner.",
        "categoria": "farmacia",
        "preco": "206.00",
    },
    {
        "key": "bravecto-20-40",
        "arquivo": "WhatsApp Image 2026-07-08 at 10.11.16.jpeg",
        "nome": "Bravecto Cães 20 a 40 kg",
        "descricao": "Comprimido mastigável contra carrapatos e pulgas. 12 semanas de proteção. 1000 mg de fluralaner.",
        "categoria": "farmacia",
        "preco": "282.90",
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
    dest = OUT / dest_name
    prepare(src, dest)
    item["imagem"] = dest_name
    print("OK", dest_name, item["preco"])

out_json = BASE / "petshop" / "catalogo_lote1.json"
out_json.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print("TOTAL", len(catalog))
print("JSON", out_json)
