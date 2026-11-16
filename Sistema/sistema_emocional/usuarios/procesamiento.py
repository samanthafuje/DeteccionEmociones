
import re
import unicodedata
from collections import Counter

from .models import AnalisisTexto


DICCIONARIO_EMOCIONAL = {
    'tristeza': [
        'triste', 'tristeza', 'llorar', 'llanto',
        'solo', 'sola', 'vacio', 'desanimado',
        'desanimada', 'desesperanza'
    ],

    'ansiedad': [
        'ansiedad', 'nervioso', 'nerviosa',
        'preocupado', 'preocupada', 'miedo',
        'temor', 'inquietud', 'angustia'
    ],

    'frustracion': [
        'frustrado', 'frustrada', 'frustracion',
        'enojo', 'enojado', 'enojada',
        'impotencia', 'molesto', 'molesta'
    ],

    'estres': [
        'estres', 'presion', 'agotado', 'agotada',
        'cansado', 'cansada', 'sobrecargado',
        'sobrecargada'
    ],

    'bienestar': [
        'feliz', 'felicidad', 'tranquilo', 'tranquila',
        'motivado', 'motivada', 'alegria',
        'satisfecho', 'satisfecha', 'apoyo'
    ]
}


EXPRESIONES_EMOCIONALES = {
    'tristeza': [
        'me siento sin ganas',
        'me siento sin animo',
        'me siento vacio',
        'me siento vacia',
        'no tengo ganas de hacer nada'
    ],

    'ansiedad': [
        'me cuesta respirar',
        'tengo miedo de reprobar',
        'no puedo dejar de preocuparme'
    ],

    'frustracion': [
        'siento mucha impotencia',
        'no logro hacer las cosas'
    ],

    'estres': [
        'tengo demasiada presion',
        'tengo muchas responsabilidades',
        'no tengo tiempo para nada'
    ],

    'bienestar': [
        'me siento en paz',
        'me siento satisfecho',
        'me siento satisfecha',
        'me siento con energia'
    ]
}


NEGACIONES = [
    'no', 'nunca', 'jamas', 'tampoco'
]


def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)

    return ''.join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != 'Mn'
    )


def esta_negada(texto, inicio):

    contexto = texto[:inicio]

    # Evita extender la negación a través de otra oración.
    contexto = re.split(r'[.!?;:]', contexto)[-1]

    palabras_previas = re.findall(
        r'\b[a-zñ]+\b',
        contexto
    )

    ultimas_palabras = palabras_previas[-4:]

    return any(
        palabra in NEGACIONES
        for palabra in ultimas_palabras
    )


def analizar_texto(texto):

    texto_normalizado = normalizar_texto(texto)

    palabras = re.findall(
        r'\b[a-zñ]+\b',
        texto_normalizado
    )

    frecuencias = Counter(palabras)

    indicadores = {}
    coincidencias_negadas = {}

    for categoria, terminos in DICCIONARIO_EMOCIONAL.items():

        afirmadas = 0
        negadas = 0

        # Palabras individuales
        for termino in terminos:

            patron = r'(?<![a-zñ])' + re.escape(termino) + r'(?![a-zñ])'

            for coincidencia in re.finditer(
                patron, texto_normalizado
            ):

                if esta_negada(
                    texto_normalizado,
                    coincidencia.start()
                ):
                    negadas += 1
                else:
                    afirmadas += 1

        # Expresiones compuestas
        for expresion in EXPRESIONES_EMOCIONALES[categoria]:

            patron = r'(?<![a-zñ])' + re.escape(expresion) + r'(?![a-zñ])'

            for coincidencia in re.finditer(
                patron, texto_normalizado
            ):

                if esta_negada(
                    texto_normalizado,
                    coincidencia.start()
                ):
                    negadas += 1
                else:
                    afirmadas += 1

        indicadores[categoria] = afirmadas
        coincidencias_negadas[categoria] = negadas

    return {
        'total_palabras': len(palabras),
        'indicadores': indicadores,
        'coincidencias_negadas': coincidencias_negadas
    }


def guardar_analisis(texto_objeto):

    resultado = analizar_texto(texto_objeto.contenido)

    analisis, creado = AnalisisTexto.objects.update_or_create(
        texto=texto_objeto,
        defaults={
            'total_palabras': resultado['total_palabras'],
            'indicadores_detectados': {
                'afirmados': resultado['indicadores'],
                'negados': resultado['coincidencias_negadas']
            },
            'version_procesamiento': 'prototipo-2.0',
            'estado': 'procesado'
        }
    )

    return analisis
