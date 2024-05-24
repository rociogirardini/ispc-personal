
# Ejercicio 1


INICIO
    // Declarar variables para almacenar las notas
    Definir nota1, nota2, nota3, nota4, nota5 Como Real
    Definir suma_notas, promedio Como Real

    // Solicitar las notas al usuario
    Escribir "Introduce la nota de la materia 1: "
    Leer nota1

    Escribir "Introduce la nota de la materia 2: "
    Leer nota2

    Escribir "Introduce la nota de la materia 3: "
    Leer nota3

    Escribir "Introduce la nota de la materia 4: "
    Leer nota4

    Escribir "Introduce la nota de la materia 5: "
    Leer nota5

    // Calcular la suma de las notas
    suma_notas <- nota1 + nota2 + nota3 + nota4 + nota5

    // Calcular el promedio
    promedio <- suma_notas / 5

    // Mostrar el resultado
    Escribir "El promedio de las notas es: ", promedio

FIN


# Ejercicio 2

INICIO

    // Declarar variables para las dimensiones de la pared y el costo por metro cuadrado
    Definir ancho, alto, costo_por_metro_cuadrado, area_pared, costo_total Como Real

    // Solicitar el ancho de la pared al usuario
    Escribir "Ingrese el ancho de la pared en metros: "
    Leer ancho

    // Solicitar el alto de la pared al usuario
    Escribir "Ingrese el alto de la pared en metros: "
    Leer alto

    // Solicitar el costo por metro cuadrado al usuario
    Escribir "Ingrese el costo por metro cuadrado: "
    Leer costo_por_metro_cuadrado

    // Calcular el área de la pared
    area_pared <- ancho * alto

    // Calcular el costo total de pintar la pared
    costo_total <- area_pared * costo_por_metro_cuadrado

    // Mostrar el resultado
    Escribir "El costo total para pintar la pared es: $", costo_total

FIN


# Ejercicio 3 

INICIO
    // Declarar variables para los partidos ganados, empatados y perdidos
    Definir partidos_ganados, partidos_empatados, partidos_perdidos Como Entero
    Definir puntos_ganados, puntos_empatados, puntos_perdidos, puntos_totales Como Entero

    // Solicitar la cantidad de partidos ganados al usuario
    Escribir "Ingrese la cantidad de partidos ganados: "
    Leer partidos_ganados

    // Solicitar la cantidad de partidos empatados al usuario
    Escribir "Ingrese la cantidad de partidos empatados: "
    Leer partidos_empatados

    // Solicitar la cantidad de partidos perdidos al usuario
    Escribir "Ingrese la cantidad de partidos perdidos: "
    Leer partidos_perdidos

    // Calcular los puntos obtenidos por partidos ganados, empatados y perdidos
    puntos_ganados <- partidos_ganados * 3
    puntos_empatados <- partidos_empatados * 1
    puntos_perdidos <- partidos_perdidos * 0 

    // Calcular el total de puntos
    puntos_totales <- puntos_ganados + puntos_empatados + puntos_perdidos

    // Mostrar el resultado
    Escribir "El equipo ha acumulado un total de ", puntos_totales, " puntos."

FIN
