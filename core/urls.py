from django.contrib import admin
from django.urls import path
from .views import alumnos
from .views import maestros
from .views import admin
from .views import auth

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
    path('alumno/', alumnos.AlumnosView.as_view()),
    # Alumnos Data
    path('lista-alumnos/', alumnos.AlumnosAll.as_view()),
    # Create Maestro
    path('maestro/', maestros.MaestrosView.as_view()),
    # Maestros Data
    path('lista-maestros/', maestros.MaestrosAll.as_view())
]
