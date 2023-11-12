from django.contrib import admin
from app.models import Carrera
from app.models import Estudiante
from app.models import Profesor
from app.models import Asignatura

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Asignatura)
# Register your models here.

#PARA QUE SALIERAN EN EL POSTGRESADMIN Y METER LOS DATOS PARA LA DB