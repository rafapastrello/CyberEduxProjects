from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')


def userspace_view(request):
    return render(request, 'userspace.html')