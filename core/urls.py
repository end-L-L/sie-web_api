from django.contrib import admin
from django.urls import path
from .views import alumnos
from .views import maestros
from .views import admin

urlpatterns = [
    # Create Admin
    path('admin/', admin.AdminView.as_view()),
    # Create Alumno
    path('alumno/', alumnos.AlumnosView.as_view()),
    # Create Maestro
    path('maestro/', maestros.MaestrosView.as_view()),
]
