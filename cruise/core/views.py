from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/login.html')

def signin(request):
    return render(request, 'core/signin.html')


def adminlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')  # Redirect to the admin page after login
    else:
        form = AuthenticationForm()
    return render(request, 'adminlogin', {'form': form})


