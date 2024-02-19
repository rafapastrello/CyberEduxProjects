from django.shortcuts import render
from .models import Publicacao

# Create your views here.

def home(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'home.html', {
        'publicacoes': publicacoes
    })
