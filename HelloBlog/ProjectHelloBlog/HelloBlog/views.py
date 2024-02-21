from django.shortcuts import render
from .models import Publicacao, Perfil
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'home.html', {
        'publicacoes': publicacoes
    })

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        dt_nascimento = request.POST.get('dt_nascimento')
        descricao = request.POST.get('descricao')
        foto = request.FILES['foto']
        senha = request.POST.get('senha')
        user = User.objects.create_user(email, password=senha)
        user.first_name = nome
        user.last_name = sobrenome
        perfil = Perfil()
        perfil.usuario = user
        perfil.dt_nascimento = dt_nascimento
        perfil.descricao = descricao
        perfil.foto = foto
        perfil.save()
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseBadRequest()

def detalhes_post(request, id):
    publicacao = Publicacao.objects.get(id=id)
    return render(request, 'detalhes_post.html', {
        'publicacao': publicacao
    })

def login_e_seguranca(request):
    return render(request, 'login_e_seguranca.html')

def meus_posts(request):
    return render(request, 'meus_posts.html')

def meus_comentarios(request):
    return render(request, 'meus_comentarios.html')

@login_required(login_url='/login')
def minha_conta(request):
    perfil = Perfil.objects.get(usuario=request.user)
    return render(request, 'minha_conta.html', {
        'authenticated': True,
        'perfil': perfil,
        'nome': request.user.username,
        'email': request.user.email,
    })

"""
def minha_conta(request):
    if request.user.is_authenticated:
        pass
        #A pessoa está logada!
        perfil = Perfil.objects.get(usuario=request.user)
        return render(request, 'minha_conta.html', {
            'authenticated': True
        })
    else:
        #A pessoa não está logada!
        return render(request, 'minha_conta.html', {
            'authenticated': False
        })
"""

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
