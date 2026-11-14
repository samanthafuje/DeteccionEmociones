
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EstudianteForm
from .models import Estudiante, RespuestaEstilo


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

    return render(
        request,
        'usuarios/dass21.html'
    )


# ==========================================================
# CERRAR SESIÓN
# ==========================================================

def logout_view(request):

    logout(request)

    return redirect('login')

