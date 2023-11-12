from django.shortcuts import render
from .models import Carrera, Profesor, Estudiante, Asignatura

def all_data(request):
    # Obtener datos de las tablas
    carreras = Carrera.objects.all()
    profesores = Profesor.objects.all()
    estudiantes = Estudiante.objects.all()
    asignaturas = Asignatura.objects.all()

    # Renderizar la plantilla con los datos
    return render(request, 'app/all_data.html', {
        'carreras': carreras,
        'profesores': profesores,
        'estudiantes': estudiantes,
        'asignaturas': asignaturas,
    })

#CONEXION PARA VER LOS DATOS DE DJANGO EN EL HTML, (ESTA PARTE SI ESTA BIEN SOLO QUE EN EL TEMPLES NO FUNCIONO pipipi)