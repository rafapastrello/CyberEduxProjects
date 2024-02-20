from django.contrib import admin
from .models import Publicacao

# admin.site.register(Publicacao)

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']
