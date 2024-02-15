from django.shortcuts import render
#from .models import Post
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.

def index(request):
    return render(request, 'feed-posts.html')

def feed_page(request):
    #posts = Post.objects.all()
    return render(request, 'feed-posts.html', {
        #'posts': posts
    })

def publicar_page(request):
    if request.method == "GET":
        return render(request, 'publicar.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        autor = request.POST.get('autor')
        #post = Post()
        #post.titulo = titulo
        #post.conteudo = conteudo
        #post.autor = autor
        #post.save()
        return HttpResponseRedirect('/publicar')
    else:
        return HttpResponseBadRequest()
