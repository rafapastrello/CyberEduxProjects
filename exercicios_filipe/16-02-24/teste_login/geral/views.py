from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'incorrect_login': False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/userspace')
        else:
            return render(request, 'login.html', {
                'incorrect_login': True
            })
    else:
        return HttpResponseBadRequest()

@login_required(login_url='/login')
def userspace_view(request):
    return render(request, 'userspace.html', {
        'username': request.user.username
    })