from django.contrib import admin
from .models import Servico, Depoimento, Categoria, Produto, Galeria

admin.site.register(Servico)
admin.site.register(Depoimento)
admin.site.register(Categoria) 
admin.site.register(Produto)   
admin.site.register(Galeria)