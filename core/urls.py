from django.contrib import admin
from django.urls import path
from .views import auth
from .views import alumno
from .views import maestro
from .views import admin
from .views import materia

urlpatterns = [
    # Login
    path('token/', auth.CustomAuthToken.as_view()),
    # Logout
    path('logout/', auth.Logout.as_view()),
    # Create Admin
    path('admin/', admin.AdminView.as_view()),
    # Admins Data
    path('lista-admins/', admin.AdminAll.as_view()),
    # Edit Admin
    path('admin-edit/', admin.AdminViewEdit.as_view()),
    # Create Alumno
    path('alumno/', alumno.AlumnoView.as_view()),
    # Alumnos Data
    path('lista-alumnos/', alumno.AlumnosAll.as_view()),
    # Edit Alumno
    path('alumno-edit/', alumno.AlumnoViewEdit.as_view()),
    # Create Maestro
    path('maestro/', maestro.MaestroView.as_view()),
    # Maestros Data
    path('lista-maestros/', maestro.MaestrosAll.as_view()),
    # Edit Maestro
    path('maestro-edit/', maestro.MaestroViewEdit.as_view()),
    # Create Materia
    path('materia/', materia.MateriaView.as_view()),
    # Materias Data
    path('lista-materias/', materia.MateriasAll.as_view()),
    # Edit Materia
    path('materia-edit/', materia.MateriaViewEdit.as_view())
]
