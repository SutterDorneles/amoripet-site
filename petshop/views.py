from django.shortcuts import render
from .models import Servico, Depoimento, Produto, Categoria, Galeria


def home(request):
    servicos = Servico.objects.filter(ativo=True)
    produtos = (
        Produto.objects.filter(disponivel=True)
        .select_related("categoria")
        .order_by("-destaque", "-criado_em")
    )
    categorias = Categoria.objects.filter(produtos__disponivel=True).distinct().order_by("nome")
    depoimentos = Depoimento.objects.all().order_by("-id")[:3]
    fotos_galeria = Galeria.objects.all().order_by("-criado_em")[:6]

    return render(
        request,
        "petshop/index.html",
        {
            "servicos": servicos,
            "produtos": produtos,
            "categorias": categorias,
            "depoimentos": depoimentos,
            "fotos_galeria": fotos_galeria,
        },
    )
