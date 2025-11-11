from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlumnoForm

def index(request):
    """Vista principal del catálogo"""
    return redirect('registrar_alumno')

def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno registrado exitosamente.')
            return redirect('registrar_alumno')
    else:
        form = AlumnoForm()

    return render(request, 'catalog/registro.html', {'form': form})