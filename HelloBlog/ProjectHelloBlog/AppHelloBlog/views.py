from django.shortcuts import render
from models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.nome_img = '/AppHelloBlog/img/thumbnails/' + post.nome_img
    return render(request, 'home.html', {'posts': posts})
