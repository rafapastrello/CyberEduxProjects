from django.contrib import admin
from .models import Figura

# Register your models here.

@admin.register(Figura)
class FiguraAdmin(admin.ModelAdmin):
    list_display=['titulo']
