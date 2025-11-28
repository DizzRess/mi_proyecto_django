from django.shortcuts import render
from .models import Actividad  # Asegúrate de importar tu modelo

def lista_actividades(request):
    actividades = Actividad.objects.all()  # Trae todas las actividades de la BD
    return render(request, "lista_actividades.html", {"actividades": actividades})
