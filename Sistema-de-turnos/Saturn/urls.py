"""Saturn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as vista
from vistas import views
from turnos import views as vistaTurnos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.welcome),
    path('', views.initial, name='initial'),
    path('register/', vista.register, name='register'),
    path('login/', vista.login, name='login'),
    path('logout/', vista.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('new_turn/', vistaTurnos.new_turn, name='new_turn'),
    path('turn_ok/', vistaTurnos.turn_ok, name='turn_ok'),
    path('combo_medico/', vistaTurnos.combo_medico, name='combo_medico'),
    path('combo_horario/', vistaTurnos.combo_horario, name='combo_horario'),
    path('listado_del_dia/', vistaTurnos.listado_del_dia, name='listado_del_dia'),
    path('delete_turn/<int:TurnoId>/', vistaTurnos.delete_turn, name='delete_turn'),
    
    
    path('admin/', admin.site.urls),
]

