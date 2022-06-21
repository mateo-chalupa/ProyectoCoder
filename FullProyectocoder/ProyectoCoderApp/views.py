import datetime

from django.shortcuts import render

from django.http import HttpResponse

from ProyectoCoderApp.models import Curso

# Create your views here.


def inicio(request):

    nombre="Mateo"

    hoy=datetime.datetime.now()
    
    notas=[4,5,6,8,9,10]


    return render(request,'ProyectoCoderApp/index.html',{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})


def crear_curso(request):

    #nombre="Python"
    #comision=31080
   # nuevo_curso= Curso (nombre=nombre,comision=comision)
    #nuevo_curso.save()
    
    curso= Curso()
    lista_cursos=[x.nombre for x in Curso.objects.all()]

    
    return HttpResponse(f"Cursos:{str(lista_cursos)}")
    