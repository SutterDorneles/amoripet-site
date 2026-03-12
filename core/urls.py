from django.contrib import admin
from django.urls import path, include # Adicione o 'include' aqui
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petshop.urls')), # Isso conecta a página inicial ao seu app
]

# Isso aqui é VITAL para as fotos dos pets/produtos aparecerem enquanto você desenvolve
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)