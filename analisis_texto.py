
"""
Considerando el diagrama de estructura anterior, implementa el módulo analisis_texto, el cual debe contener, principalmente, las siguientes funciones:
contar_oraciones(texto): cuenta las oraciones del texto que recibe como parámetro.
contar_palabras(texto): cuenta las palabras del texto que recibe como parámetro.
contar_sílabas(texto): cuenta las sílabas del texto que recibe como parámetro.

"""

def contar_oraciones(texto):
    oraciones = 0
    for caracter in texto:
        if caracter in ".!?:;":
            oraciones += 1
    return oraciones if oraciones > 0 else 1

def contar_palabras(texto):
    palabras = 0
    for caracter in texto:
        if caracter.isspace() or caracter in ".!?,;:":
            palabras += 1
    return palabras

def contar_silabas(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    silabas = 0
    for caracter in texto:
        if caracter in vocales:
            silabas += 1
    return silabas
