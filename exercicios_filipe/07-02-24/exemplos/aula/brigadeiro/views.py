from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def index_page_username(request, username):
    return render(request, 'index.html', {
        'username': username
    })