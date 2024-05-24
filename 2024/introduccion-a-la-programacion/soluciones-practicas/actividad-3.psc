## 1. Mostrar los números desde el 0 al número solicitado al usuario (input)

INICIO
    Definir numero Como Entero

    Escribir "Ingrese un número: "
    Leer numero

    Para i <- 0 Hasta numero Con Paso 1 Hacer
        Escribir i
    FinPara

FIN
    
    
## 2. Mostrar sólo los números pares desde 0 hasta el número ingresado (input)

INICIO
    Definir numero Como Entero

    Escribir "Ingrese un número: "
    Leer numero

    Para i <- 0 Hasta numero Con Paso 1 Hacer
        Si i % 2 == 0 Entonces
            Escribir i
        FinSi
    FinPara

FIN

        
## 3. Pedir que el usuario ingrese nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

INICIO
    Definir nombre Como Cadena

    nombre <- ""
    Mientras nombre <> "fin" Hacer
        Escribir "Ingrese un nombre (o 'fin' para terminar): "
        Leer nombre
        Si nombre <> "fin" Entonces
            Escribir nombre
        FinSi
    FinMientras

FIN

        
## 4. Promedio escolar 

INICIO
    Definir cantidad_alumnos Como Entero
    Definir suma_notas, promedio Como Real

    Escribir "Ingrese la cantidad de alumnos: "
    Leer cantidad_alumnos

    suma_notas <- 0

    Para i <- 1 Hasta cantidad_alumnos Con Paso 1 Hacer
        Escribir "Ingrese la nota del alumno ", i, ": "
        Leer nota
        suma_notas <- suma_notas + nota
    FinPara

    promedio <- suma_notas / cantidad_alumnos

    Si promedio > 8 Entonces
        Escribir "El rendimiento ha sido elevado."
    Sino
        Si promedio >= 6 Entonces
            Escribir "El rendimiento ha sido aceptable."
        Sino
            Escribir "El rendimiento ha sido bajo."
        FinSi
    FinSi

FIN


## 5. Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10.

# Solución mientras (while)

INICIO
    Definir numero, i, resultado Como Entero

    Escribir "Ingrese un número entre 1 y 10: "
    Leer numero

    i <- 1

    Mientras i <= 10 Hacer
        resultado <- numero * i
        Escribir numero, "x", i, "=", resultado
        i <- i + 1
    FinMientras

FIN

# Solución para (for)
    
INICIO
    Definir numero, resultado Como Entero

    Escribir "Ingrese un número entre 1 y 10: "
    Leer numero

    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        resultado <- numero * i
        Escribir numero, "x", i, "=", resultado
    FinPara

FIN
