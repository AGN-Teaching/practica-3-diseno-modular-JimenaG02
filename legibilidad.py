import  analisis_texto as at
"""
indice_legibilidad_VG(texto): calcula el índice de Velázquez Gaytán para el texto recibido como parámetro. Esta función debe devolver, en este orden, la
cantidad de oraciones, de palabras y de sílabas del texto, además del índice de Velázquez Gaytán correspondiente.
nivel_legibilidad_VG(indice): decide el nivel de legibilidad de un texto, cuyo índice de Velázquez Gaytán recibe como parámetro.
Debe devolver el nivel como un string.

"""
def indice_legibilidad_VG(texto):
    #Mandamos a llamar las funciones del modulo "analisis_texto.py" para poder trabajar con ellas y sacar los valores de oraciones, palabras y silabas
    oraciones = at.contar_oraciones(texto)
    palabras = at.contar_palabras(texto)
    silabas = at.contar_silabas(texto)
    
    L = 206.84 - 1.02 *(palabras / oraciones) - 60 *(silabas / palabras) #Formula Indice de Velazquez Gaytan

    return oraciones,palabras,silabas,L


def nivel_legibilidad_VG(indice): #Determina el nivel de legibilidad segun el indice
    nivel = ""
    if indice >=90 and indice <=100:
        nivel = "Muy facil"
    elif indice >=80 and indice <= 90:
        nivel = "Facil"
    elif indice >=70 and indice <=80:
        nivel = "Relativamente Facil"
    elif indice >=60 and indice <= 70:
        nivel = "Normal"
    elif indice >=50 and indice <=60:
        nivel= "Relativamente Dificil"
    elif indice>= 30 and indice <= 50:
        nivel = "Dificil"
    else:
        nivel = "Muy Dificil"

    return nivel
