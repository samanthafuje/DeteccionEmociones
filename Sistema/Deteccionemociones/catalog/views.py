from django.shortcuts import render, redirect, get_object_or_404
from .models import alumno
from .forms import AlumnoForm, EstilosAprendizajeForm


def registrar_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        estudiante = form.save()
        return redirect('estilos_aprendizaje', alumno_id=estudiante.id_alumno)
    return render(request, 'catalog/registro.html', {'form': form})


def estilos_aprendizaje_view(request, alumno_id):
    alumno_obj = get_object_or_404(alumno, pk=alumno_id)

    if request.method == 'POST':
        form = EstilosAprendizajeForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.alumno = alumno_obj

            respuestas = [
                test.p1, test.p2, test.p3, test.p4, test.p5,
                test.p6, test.p7, test.p8, test.p9, test.p10
            ]

            visual = respuestas.count('A')
            auditivo = respuestas.count('B')
            kinestesico = respuestas.count('C')

            if visual >= auditivo and visual >= kinestesico:
                resultado = 'Visual'
            elif auditivo >= kinestesico:
                resultado = 'Auditivo'
            else:
                resultado = 'Kinestésico'

            test.resultado = resultado
            alumno_obj.tipo_aprendizaje = resultado.lower()
            alumno_obj.save()
            test.save()

            return redirect('resultado_estilo', alumno_id=alumno_obj.id_alumno)
    else:
        form = EstilosAprendizajeForm()

    return render(request, 'catalog/aprendizaje.html', {
        'form': form,
        'alumno': alumno_obj
    })


def resultado_estilo(request, alumno_id):
    alumno_obj = get_object_or_404(alumno, pk=alumno_id)

    # Obtenemos el primer test del alumno
    test = alumno_obj.estilosaprendizaje.first()

    if not test:
        # Si no hay test, redirigimos al formulario
        return redirect('estilos_aprendizaje', alumno_id=alumno_obj.id_alumno)

    # Calculamos los conteos de cada estilo de manera más limpia
    respuestas = [test.p1, test.p2, test.p3, test.p4, test.p5,
                  test.p6, test.p7, test.p8, test.p9, test.p10]

    visual = respuestas.count('A')
    auditivo = respuestas.count('B')
    kinestesico = respuestas.count('C')

    return render(request, 'catalog/resultado_estilo.html', {
        'resultado': test.resultado,
        'alumno': alumno_obj,
        'visual': visual,
        'auditivo': auditivo,
        'kinestesico': kinestesico
    })