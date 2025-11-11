from django.shortcuts import render, redirect
from .forms import AlumnoForm

def registrar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_alumno')  # o puedes regresar a otra url
    else:
        form = AlumnoForm()

    return render(request, '/registro.html', {'form': form})