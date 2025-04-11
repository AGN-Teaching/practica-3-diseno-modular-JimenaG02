[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zLSmh4bI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19021176)
# Práctica 3. Diseño modular
## Objetivo del programa

Este programa analiza la legibilidad de textos en español utilizando el **Índice de Velázquez Gaytán**, una adaptación del índice Flesch para la lengua española. Su función principal es determinar qué tan fácil o difícil es comprender un texto según características lingüísticas como:

1. **Longitud de las oraciones** (cantidad promedio de palabras por oración)
2. **Complejidad de las palabras** (cantidad promedio de sílabas por palabra)

## Funcionamiento general

El programa realiza las siguientes operaciones:

1. **Entrada de datos**: Solicita al usuario el nombre de un archivo de texto (.txt)
2. **Procesamiento**:
   - Cuenta automáticamente las oraciones, palabras y sílabas
   - Aplica la fórmula de Velázquez Gaytán:  
     `L = 206.84 - 1.02*(palabras/oraciones) - 60*(sílabas/palabras)`
3. **Clasificación**: Asigna un nivel de legibilidad entre 7 posibles
4. **Salida**: Muestra resultados numéricos y su interpretación
## Módulos principales

### 1. analisis_texto.py
Realiza el análisis lingüístico básico:
- `contar_oraciones()`: Detecta finales de oración (.!?:;)
- `contar_palabras()`: Identifica palabras entre espacios/puntuación
- `contar_silabas()`: Aproxima sílabas contando vocales (incluye tildes)

### 2. legibilidad.py
Calcula y clasifica:
- `indice_legibilidad_VG()`: Aplica la fórmula matemática
- `nivel_legibilidad_VG()`: Asigna categorías según rangos predefinidos

## Resultados obtenidos

### AlanTuring.txt
- **Índice:** 58.91 → *Relativamente Difícil*
- **Estadísticas:** 20 oraciones, 597 palabras, 1169 sílabas

### ComputacionEvolutiva.txt
- **Índice:** 36.54 → *Difícil*
- **Estadísticas:** 9 oraciones, 220 palabras, 533 sílabas

### PatitoFeo.txt
- **Índice:** 100.25 → *Muy fácil* (aunque técnicamente supera el máximo teórico, esto se debe a que el texto es muy corto)
- **Estadísticas:** 39 oraciones, 596 palabras, 904 sílabas
