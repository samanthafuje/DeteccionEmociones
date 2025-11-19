from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlumnoForm
from .forms import estilos_aprendizajeForm
from catalog.models import alumno

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


def estilos_aprendizaje(request):
    result = None
    
    if request.method == 'POST':
        form = estilos_aprendizajeForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            # Calcular estilo de aprendizaje            
            visual = sum([test.q1 == "A", test.q4 == "A", test.q7 == "A"])
            auditivo = sum([test.q2 == "A", test.q5 == "A", test.q8 == "A"])
            kinestesico = sum([test.q3 == "A", test.q6 == "A", test.q9 == "A"])
            if max(visual, auditivo, kinestesico) == visual:
                resultado = "visual"
            elif max(visual, auditivo, kinestesico) == auditivo:
                resultado = "auditivo"
            elif  max(visual, auditivo, kinestesico) == kinestesico:
                resultado = "kinestesico"
            else:
                resultado = "visual"
# Guardar en el test            
            test.result = resultado.capitalize()
            test.save()
# ACTUALIZAR ALUMNO
            alumno_obj = test.alumno
            alumno_obj.tipo_aprendizaje = resultado
            alumno_obj.save()
            result = resultado.capitalize()
    else:
        form = estilos_aprendizajeForm()
        return render(request, 'catalog/aprendizaje.html', {
            'form': form,
            'result': result
            })