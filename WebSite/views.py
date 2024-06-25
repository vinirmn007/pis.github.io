import requests
from django.shortcuts import render, redirect
from Carrito.models import *
from Sensores.views import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')

def desarrolladores(request):
    return render(request, 'desarrolladores.html')

def documentacion(request):
    return render(request, 'documentacion.html')

def funcionamiento (request):
    return render(request, 'funcionamiento.html')

def testimonios(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonios') 
    else:
        form = TestimonioForm()

    testimonios = Testimonio.objects.all().order_by('fecha')
    content = {
        'form': form, 
        'testimonios': testimonios
        }
    return render(request, 'testimonios.html', content)

def diagramaClases (request):
    return render(request, 'diagramaClases.html')

def materias (request):
    return render(request, 'materias.html')

def historiaUsuario(request):
    return render(request, 'historiasUsuario.html')

def control_servo(request):
    if 'angle' in request.GET:
        angle = request.GET['angle']
        esp32_ip = 'http://192.168.100.61' # Cambia a la IP de tu ESP32
        response = requests.get(f'{esp32_ip}/?angle={angle}')
        return HttpResponse(f'Servomotor movido a {angle} grados')
    return render(request, 'control.html')