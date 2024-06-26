from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AdminSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Administradores
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = "__all__"

class MaestroSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Maestros
        fields = '__all__'

# Serializers para Materia
class MateriaSerializer(serializers.ModelSerializer):
    nrc = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True)

    class Meta:
        model = Materias
        fields = ('nrc','nombre')

class MateriasSerializer(serializers.ModelSerializer):
    materia=MateriaSerializer(read_only=True)
    class Meta:
        model = Materias
        fields = "__all__"