from django.shortcuts import render

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/login.html')

def signin(request):
    return render(request, 'core/signin.html')
