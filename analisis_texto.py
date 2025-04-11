
"""
Considerando el diagrama de estructura anterior, implementa el módulo analisis_texto, el cual debe contener, principalmente, las siguientes funciones:
contar_oraciones(texto): cuenta las oraciones del texto que recibe como parámetro.
contar_palabras(texto): cuenta las palabras del texto que recibe como parámetro.
contar_sílabas(texto): cuenta las sílabas del texto que recibe como parámetro.

"""

def contar_oraciones(texto): #Cuenta las oraciones en un texto basado en signos de puntuacion finales (.!?:;)
    oraciones = 0
    for caracter in texto:
        if caracter in ".!?:;": #Signos que toma en cuenta como puntuacion finales
            oraciones += 1
    return oraciones if oraciones > 0 else 1 #Al menos un signo de puntuacion 

def contar_palabras(texto): #Considera palabras como secuencias entre espacios
    palabras = 0
    for caracter in texto:    
        if caracter.isspace() or caracter in ".!?,;:": #Si hay un epsacio o contiene esos caracteres los cuenta como palabras
            palabras += 1
    return palabras

def contar_silabas(texto): #Aproxima el numero de silabas contando vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ" #vocales minusculas con y sin tilde, mayusculas con y sin tilde
    silabas = 0
    for caracter in texto:
        if caracter in vocales:
            silabas += 1
    return silabas
