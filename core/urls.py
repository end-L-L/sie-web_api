from django.contrib import admin
from django.urls import path
from .views import alumnos
from .views import maestros

urlpatterns = [
    # Create Admin
    path('admin/', admin.site.urls),
    # Create Alumno
    path('alumno/', alumnos.AlumnosView.as_view()),
    # Create Maestro
    path('maestro/', maestros.MaestrosView.as_view()),
]
