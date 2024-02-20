from django.shortcuts import render
from .models import Publicacao

# Create your views here.

def home(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'home.html', {
        'publicacoes': publicacoes
    })

def detalhes_post(request):
    return render(request, 'detalhes_post.html')

def login(request):
    return render(request, 'login.html')

def publicar(request):
    return render(request, 'publicar.html')

def redes_sociais(request):
    return render(request, 'redes_sociais.html')

def sobre(request):
    return render(request, 'sobre.html')
