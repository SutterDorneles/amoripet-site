from django.db import models

# ✅ NOVO: Categoria para organizar seus produtos (Rações, Brinquedos, etc)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Nome na URL (ex: racoes-caes)")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"

# ✅ NOVO: A classe que estava faltando!
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Aqui está o campo de promoção que conversamos:
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    estoque = models.IntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False, help_text="Aparecer na página inicial?")
    selo_oferta = models.BooleanField(default=False, help_text="Mostrar selo de Oferta?")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Seu código que já estava funcionando:
class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, help_text="Nome do ícone Bootstrap (ex: bi-scissors)")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Depoimento(models.Model):
    nome_dono = models.CharField(max_length=100)
    nome_pet = models.CharField(max_length=100)
    texto = models.TextField()
    foto_pet = models.ImageField(upload_to='depoimentos/')

    def __str__(self):
        return f"{self.nome_dono} - {self.nome_pet}"
    
# ✅ ADICIONE esta classe ao final do seu petshop/models.py
class Galeria(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    imagem = models.ImageField(upload_to='galeria/')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Galeria de Fotos"

    def __str__(self):
        return self.titulo if self.titulo else f"Foto {self.id}"    