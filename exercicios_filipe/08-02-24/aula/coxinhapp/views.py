from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Pessoa

# Create your views here.

def index(request):
    return HttpResponseRedirect('/consulta')

def cadastro_page(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        pessoa = Pessoa()
        pessoa.nome = nome
        pessoa.estado = estado
        pessoa.cidade = cidade
        pessoa.save()
        return HttpResponseRedirect('/consulta')
    else:
        return HttpResponseBadRequest()

def consulta_page(request):
    #pessoas = Pessoa.objects.filter(estado = "Rio de Janeiro")
    #pessoas = Pessoa.objects.raw("SELECT * FROM coxinhapp_pessoa WHERE cidade = 'Cuiabá'")
    pessoas = Pessoa.objects.all()
    return render(request, 'consulta.html', {
        'pessoas': pessoas
    })
