from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

