from django.shortcuts import render
from .models import Publication
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def write_page(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    elif request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        publication = Publication()
        publication.author = author
        publication.content = content
        publication.save()
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()

def feed_page(request):
    publicacoes = Publication.objects.order_by('-date').all()
    return render(request, 'feed.html', {
        'publicacoes': publicacoes
    })
