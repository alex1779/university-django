from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    context = {
        'cursos' : cursos
    }
    return render(request, 'gestionCursos.html', context)


def registrarCurso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['txtcreditos']
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    context = {
        'curso' : curso
    }
    return render(request, "edicionCurso.html", context)


def editarCurso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['txtcreditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')
