from django.shortcuts import render

# Create your views here.
from .models import Actividad

def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, "lista_actividades.html", {"actividades": actividades})