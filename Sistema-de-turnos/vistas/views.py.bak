from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Registro
from turnos.models import Medico


@login_required(login_url='login')
def dashboard(request):
    cargar_boton = False
    if str(request.user) == 'admin@admin':      
        cargar_boton = True
    context = {
        'cargar_boton': cargar_boton, 
    }
    return render(request, "dashboard.html", context)
 
