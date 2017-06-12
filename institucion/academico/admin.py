from django.contrib import admin

from academico.models import *

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Paralelo)
admin.site.register(ParaleloEstudiante)
admin.site.register(Periodo)

