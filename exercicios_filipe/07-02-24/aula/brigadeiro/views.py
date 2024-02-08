from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

def index_page(request):
    return render(request, 'index.html')


def index_page_username(request, username):
    nomes = ['Filipe', 'Enzo', 'Rafaela']
    return render(request, 'index.html', {
        'username': username,
        'nomes': nomes
    })


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        return HttpResponse(f'{nome}, {sobrenome}')
    else:
        return HttpResponseBadRequest()
