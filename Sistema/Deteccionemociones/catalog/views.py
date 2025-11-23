from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlumnoForm
from .forms import estilos_aprendizajeForm
from catalog.models import alumno
from catalog.models import EstilosAprendizaje

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


def estilos_aprendizaje(request, id_alumno):
    estudiante = alumno.objects.get(id_alumno=id_alumno)

    if request.method == 'POST':
        respuestas = {f"p{i}": request.POST.get(f"p{i}") for i in range(1, 11)}

        test = EstilosAprendizaje.objects.create(
            alumno=estudiante,
            **respuestas
        )

        visual = sum(v == "A" for v in respuestas.values())
        auditivo = sum(v == "B" for v in respuestas.values())
        kinestesico = sum(v == "C" for v in respuestas.values())

        if visual > auditivo and visual > kinestesico:
            resultado = "Visual"
        elif auditivo > visual and auditivo > kinestesico:
            resultado = "Auditivo"
        else:
            resultado = "Kinestésico"

        # Guardar resultado en el alumno
        estudiante.tipo_aprendizaje = resultado.lower()
        estudiante.save()

        # Guardar resultado también en el test
        test.resultado = resultado
        test.save()

        return render(request, "resultado_aprendizaje.html", {
            "resultado": resultado,
            "visual": visual,
            "auditivo": auditivo,
            "kinestesico": kinestesico,
            "alumno": estudiante
        })

    return render(request, "catalog/aprendizaje.html", {"alumno": estudiante})