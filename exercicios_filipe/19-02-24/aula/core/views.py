from django.shortcuts import render, redirect
from .models import Figura

# Create your views here.

def galeria_view(request):
    figuras = Figura.objects.all()
    return render(request, 'galeria.html', {
        'figuras': figuras
    })

def carregar_view(request):
    if request.method == "GET":
        return render(request, 'carregar.html')
    else:
        titulo = request.POST.get('titulo')
        imagem = request.FILES['imagem']
        figura = Figura()
        figura.titulo = titulo
        figura.imagem = imagem
        figura.save()
        return redirect('/')
