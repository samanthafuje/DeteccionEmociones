from .procesamiento import guardar_analisis
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EstudianteForm
from .models import Estudiante, RespuestaEstilo


from django.db import transaction

from .models import EvaluacionDASS21, RespuestaDASS21

from .models import TextoEstudiante, AnalisisTexto

# ==========================================================
# OBTENER ESTUDIANTE
# ==========================================================

def obtener_estudiante(request):

    try:
        return Estudiante.objects.get(usuario=request.user)

    except Estudiante.DoesNotExist:
        messages.error(
            request,
            'Tu usuario no tiene un perfil de estudiante asociado.'
        )
        return None


# ==========================================================
# REGISTRO
# ==========================================================

def registro(request):

    if request.method == 'POST':

        form = EstudianteForm(request.POST)

        if form.is_valid():

            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']

            if User.objects.filter(username=correo).exists():

                form.add_error(
                    'correo',
                    'Este correo electrónico ya está registrado.'
                )

            else:

                usuario = User.objects.create_user(
                    username=correo,
                    email=correo,
                    password=password
                )

                estudiante = form.save(commit=False)
                estudiante.usuario = usuario
                estudiante.save()

                messages.success(
                    request,
                    'Registro exitoso. Ahora puedes iniciar sesión.'
                )

                return redirect('login')

    else:
        form = EstudianteForm()

    return render(
        request,
        'usuarios/registro.html',
        {
            'form': form
        }
    )


# ==========================================================
# INICIO DE SESIÓN
# ==========================================================

def login_view(request):

    if request.method == 'POST':

        correo = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=correo,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            return redirect('inicio')

        else:

            return render(
                request,
                'usuarios/login.html',
                {
                    'error': 'Correo o contraseña incorrectos.'
                }
            )

    return render(
        request,
        'usuarios/login.html'
    )


# ==========================================================
# INICIO
# ==========================================================

@login_required
def inicio(request):

    return render(
        request,
        'usuarios/inicio.html'
    )


# ==========================================================
# TEST DE ESTILOS CHAEA
# ==========================================================

@login_required
def test_estilos(request):

    estudiante = obtener_estudiante(request)

    if estudiante is None:
        return redirect('registro')

    # PREGUNTAS ACTIVO
    preguntas_activo = [
        3, 5, 7, 9, 13,
        20, 26, 27, 35, 37,
        41, 43, 46, 48, 51,
        61, 67, 74, 75, 77
    ]

    # PREGUNTAS REFLEXIVO
    preguntas_reflexivo = [
        10, 16, 18, 19, 28,
        31, 32, 34, 36, 39,
        42, 44, 49, 55, 58,
        63, 65, 69, 70, 79
    ]

    # PREGUNTAS TEÓRICO
    preguntas_teorico = [
        2, 4, 6, 11, 15,
        17, 21, 23, 25, 29,
        33, 45, 50, 54, 60,
        64, 66, 71, 78, 80
    ]

    # PREGUNTAS PRAGMÁTICO
    preguntas_pragmatico = [
        1, 8, 12, 14, 22,
        24, 30, 38, 40, 47,
        52, 53, 56, 57, 59,
        62, 68, 72, 73, 76
    ]

    # ======================================================
    # PROCESAR TEST
    # ======================================================

    if request.method == 'POST':

        RespuestaEstilo.objects.filter(
            estudiante=estudiante
        ).delete()

        activo = 0
        reflexivo = 0
        teorico = 0
        pragmatico = 0

        for numero in range(1, 81):

            respuesta = request.POST.get(
                f'pregunta{numero}'
            )

            if respuesta:

                RespuestaEstilo.objects.create(
                    estudiante=estudiante,
                    pregunta=numero,
                    respuesta=respuesta
                )

                if respuesta == 'si':

                    if numero in preguntas_activo:
                        activo += 1

                    elif numero in preguntas_reflexivo:
                        reflexivo += 1

                    elif numero in preguntas_teorico:
                        teorico += 1

                    elif numero in preguntas_pragmatico:
                        pragmatico += 1

        resultados = {
            'Activo': activo,
            'Reflexivo': reflexivo,
            'Teórico': teorico,
            'Pragmático': pragmatico
        }

        estilo_predominante = max(
            resultados,
            key=resultados.get
        )

        return render(
            request,
            'usuarios/resultado_chae.html',
            {
                'activo': activo,
                'reflexivo': reflexivo,
                'teorico': teorico,
                'pragmatico': pragmatico,
                'estilo_predominante': estilo_predominante
            }
        )

    return render(
        request,
        'usuarios/test_estilos.html'
    )


# ==========================================================
# RESULTADO CHAEA
# ==========================================================

@login_required
def resultado_chae(request):

    estudiante = obtener_estudiante(request)

    if estudiante is None:
        return redirect('registro')

    respuestas = RespuestaEstilo.objects.filter(
        estudiante=estudiante
    )

    preguntas_activo = [
        3, 5, 7, 9, 13,
        20, 26, 27, 35, 37,
        41, 43, 46, 48, 51,
        61, 67, 74, 75, 77
    ]

    preguntas_reflexivo = [
        10, 16, 18, 19, 28,
        31, 32, 34, 36, 39,
        42, 44, 49, 55, 58,
        63, 65, 69, 70, 79
    ]

    preguntas_teorico = [
        2, 4, 6, 11, 15,
        17, 21, 23, 25, 29,
        33, 45, 50, 54, 60,
        64, 66, 71, 78, 80
    ]

    preguntas_pragmatico = [
        1, 8, 12, 14, 22,
        24, 30, 38, 40, 47,
        52, 53, 56, 57, 59,
        62, 68, 72, 73, 76
    ]

    activo = 0
    reflexivo = 0
    teorico = 0
    pragmatico = 0

    for respuesta in respuestas:

        numero = respuesta.pregunta

        if respuesta.respuesta == 'si':

            if numero in preguntas_activo:
                activo += 1

            elif numero in preguntas_reflexivo:
                reflexivo += 1

            elif numero in preguntas_teorico:
                teorico += 1

            elif numero in preguntas_pragmatico:
                pragmatico += 1

    resultados = {
        'Activo': activo,
        'Reflexivo': reflexivo,
        'Teórico': teorico,
        'Pragmático': pragmatico
    }

    estilo_predominante = max(
        resultados,
        key=resultados.get
    )

    return render(
        request,
        'usuarios/resultado_chae.html',
        {
            'activo': activo,
            'reflexivo': reflexivo,
            'teorico': teorico,
            'pragmatico': pragmatico,
            'estilo_predominante': estilo_predominante
        }
    )
# ==========================================================
# DASS-21 TEMPORAL
# ==========================================================

def dass21(request):

    return redirect('test_dass21')


# ==========================================================
# CERRAR SESIÓN
# ==========================================================

def logout_view(request):

    logout(request)

    return redirect('login')


# ==========================================================
# DASS 21
# ==========================================================
OPCIONES_DASS21 = [
    (0, 'No me ha ocurrido'),
    (1, 'Me ha ocurrido un poco'),
    (2, 'Me ha ocurrido bastante'),
    (3, 'Me ha ocurrido mucho'),
]

PREGUNTAS_DASS21 = [
    "Me ha costado mucho descargar la tensión.",
    "Me di cuenta que tenía la boca seca.",
    "No podía sentir ningún sentimiento positivo.",
    "Se me hizo difícil respirar.",
    "Se me hizo difícil tomar la iniciativa para hacer cosas.",
    "Reaccioné exageradamente en ciertas situaciones.",
    "Sentí que mis manos temblaban.",
    "He sentido que estaba gastando una gran cantidad de energía.",
    "Estaba preocupado por situaciones en las cuales podía tener pánico o en las que podría hacer el ridículo.",
    "He sentido que no había nada que me ilusionara.",
    "Me he sentido inquieto.",
    "Se me hizo difícil relajarme.",
    "Me sentí triste y deprimido.",
    "No toleré nada que no me permitiera continuar con lo que estaba haciendo.",
    "Sentí que estaba al punto de pánico.",
    "No me pude entusiasmar por nada.",
    "Sentí que valía muy poco como persona.",
    "He tendido a sentirme enfadado con facilidad.",
    "Sentí los latidos de mi corazón a pesar de no haber hecho ningún esfuerzo físico.",
    "Tuve miedo sin razón.",
    "Sentí que la vida no tenía ningún sentido."
]

def interpretar_puntaje(puntaje, categoria):

    if categoria == 'depresion':

        rangos = [
            (9, 'Normal'),
            (13, 'Leve'),
            (20, 'Moderada'),
            (27, 'Grave'),
        ]

    elif categoria == 'ansiedad':

        rangos = [
            (7, 'Normal'),
            (9, 'Leve'),
            (14, 'Moderada'),
            (19, 'Grave'),
        ]

    else:

        rangos = [
            (14, 'Normal'),
            (18, 'Leve'),
            (25, 'Moderado'),
            (33, 'Grave'),
        ]

    for limite, nivel in rangos:

        if puntaje <= limite:
            return nivel

    return 'Extremadamente grave' if categoria == 'depresion' else 'Muy grave'


def _preguntas_dass21(respuestas=None, primera_faltante=None):

    respuestas = respuestas or {}

    return [
        {
            'numero': numero,
            'texto': texto,
            'seleccionada': respuestas.get(numero),
            'abierta': numero == primera_faltante,
        }
        for numero, texto in enumerate(PREGUNTAS_DASS21, start=1)
    ]


@login_required
def test_dass21(request):

    if request.method == 'POST':

        valores = {}
        faltantes = []

        for numero in range(1, 22):

            valor = request.POST.get(f'pregunta{numero}')

            if valor not in ['0', '1', '2', '3']:
                faltantes.append(numero)
            else:
                valores[numero] = int(valor)

        if faltantes:

            return render(request, 'usuarios/test_dass21.html', {
                'preguntas': _preguntas_dass21(
                    valores,
                    faltantes[0]
                ),
                'opciones_dass': OPCIONES_DASS21,
                'error': (
                    'Debes responder las preguntas: '
                    + ', '.join(str(n) for n in faltantes)
                    + '.'
                )
            })

        respuestas = [valores[numero] for numero in range(1, 22)]

        # Clasificación de preguntas por subescala
        indices_depresion = [3, 5, 10, 13, 16, 17, 21]
        indices_ansiedad = [2, 4, 7, 9, 15, 19, 20]
        indices_estres = [1, 6, 8, 11, 12, 14, 18]

        # Sumar las respuestas originales y multiplicar por 2
        depresion = sum(
            respuestas[i - 1] for i in indices_depresion
        ) * 2

        ansiedad = sum(
            respuestas[i - 1] for i in indices_ansiedad
        ) * 2

        estres = sum(
            respuestas[i - 1] for i in indices_estres
        ) * 2

        # Obtener el estudiante asociado al usuario autenticado
        try:
            estudiante = request.user.estudiante
        except AttributeError:
            return redirect('login')

        # Guardar evaluación y respuestas
        with transaction.atomic():

            evaluacion = EvaluacionDASS21.objects.create(
                estudiante=estudiante,
                depresion=depresion,
                ansiedad=ansiedad,
                estres=estres,
                nivel_depresion=interpretar_puntaje(
                    depresion, 'depresion'
                ),
                nivel_ansiedad=interpretar_puntaje(
                    ansiedad, 'ansiedad'
                ),
                nivel_estres=interpretar_puntaje(
                    estres, 'estres'
                )
            )

            for numero, respuesta in enumerate(respuestas, start=1):

                RespuestaDASS21.objects.create(
                    evaluacion=evaluacion,
                    pregunta=numero,
                    respuesta=respuesta
                )

        return redirect(
            'resultado_dass21',
            evaluacion_id=evaluacion.id
        )

    return render(request, 'usuarios/test_dass21.html', {
        'preguntas': _preguntas_dass21(primera_faltante=1),
        'opciones_dass': OPCIONES_DASS21
    })


# ==========================================================
# DASS 21 (Resultado)
# ==========================================================

@login_required
def resultado_dass21(request, evaluacion_id):

    try:
        estudiante = request.user.estudiante
    except AttributeError:
        return redirect('login')

    evaluacion = get_object_or_404(
        EvaluacionDASS21,
        id=evaluacion_id,
        estudiante=estudiante
    )

    return render(
        request,
        'usuarios/resultado_dass21.html',
        {
            'evaluacion': evaluacion
        }
    )

# ==========================================================
# CAPTURA DE TEXTO DEL ESTUDIANTE
# ==========================================================

@login_required
def captura_texto(request):

    if request.method == 'POST':

        contenido = request.POST.get('contenido', '').strip()

        if len(contenido) < 30:
            messages.error(
                request,
                'Tu texto debe contener al menos 30 caracteres.'
            )

        elif len(contenido) > 5000:
            messages.error(
                request,
                'Tu texto no puede superar los 5000 caracteres.'
            )

        else:
            texto_guardado = TextoEstudiante.objects.create(
                estudiante=request.user.estudiante,
                contenido=contenido
            )

            guardar_analisis(texto_guardado)

            messages.success(
                request,
                'Tu texto se guardó y procesó correctamente.'
            )

            return redirect('captura_texto')

    return render(request, 'usuarios/captura_texto.html')


# ==========================================================
# REPORTES INDIVIDUALES DEL ESTUDIANTE
# ==========================================================

@login_required
def mis_reportes(request):

    estudiante = obtener_estudiante(request)

    if estudiante is None:
        return redirect('registro')

    textos = TextoEstudiante.objects.filter(
        estudiante=estudiante
    ).order_by('-fecha_creacion')

    return render(
        request,
        'usuarios/mis_reportes.html',
        {
            'textos': textos
        }
    )


# ==========================================================
# DETALLE DE UN REPORTE
# ==========================================================

@login_required
def detalle_reporte(request, texto_id):

    estudiante = obtener_estudiante(request)

    if estudiante is None:
        return redirect('registro')

    texto = get_object_or_404(
        TextoEstudiante,
        id=texto_id,
        estudiante=estudiante
    )

    try:
        analisis = texto.analisis
    except AnalisisTexto.DoesNotExist:
        analisis = None

    return render(
        request,
        'usuarios/detalle_reporte.html',
        {
            'texto': texto,
            'analisis': analisis
        }
    )
