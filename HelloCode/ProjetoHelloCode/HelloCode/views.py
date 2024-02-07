from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def minha_view(request):
    context = {'mensagem': 'Olá, Mundo!'}
    return render(request, 'meu_template.html', context)
