from django.shortcuts import render
from .models import Publicacao
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.

def home(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'home.html', {
        'publicacoes': publicacoes
    })

def detalhes_post(request, id):
    publicacao = Publicacao.objects.get(id=id)
    return render(request, 'detalhes_post.html', {
        'publicacao': publicacao
    })

def login_e_seguranca(request):
    return render(request, 'login_e_seguranca.html')

def login(request):
    return render(request, 'login.html')

def minha_conta(request):
    return render(request, 'minha_conta.html')

def publicar(request):
    if request.method == 'GET':
        return render(request, 'publicar.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        categoria = request.POST.get('categoria')
        conteudo = request.POST.get('conteudo')
        thumbnail = request.FILES['thumbnail']
        publicacao = Publicacao()
        publicacao.titulo = titulo
        publicacao.autor = autor
        publicacao.categoria = categoria
        publicacao.conteudo = conteudo
        publicacao.thumbnail = thumbnail
        publicacao.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseBadRequest()

def redes_sociais(request):
    return render(request, 'redes_sociais.html')

def sobre(request):
    return render(request, 'sobre.html')
