from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from users.forms import RegistroForm

def welcome(request):
    return render(request, "welcome.html")

def register(request):
    form = RegistroForm()
    if request.method == "POST":
        form = RegistroForm(data=request.POST)
        if form.is_valid():
            account = form.save()
            do_login(request, account)
            return redirect('dashboard')

    form = RegistroForm()
    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def login(request):
    if request.method == "POST":
        print(request)
        username = request.POST['email']
        password = request.POST['password']
        print(username)
        print(password)
        account = authenticate(username=username, password=password)
        print(account)
        if account is not None:
            do_login(request, account)
            return redirect('dashboard')
            
    return render(request, "login.html")

def logout(request):
    # Redireccionamos a la portada
    do_logout(request)
    return redirect('/')
