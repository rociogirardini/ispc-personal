# ---- Estructuras Iterativas ---- 

### Ejercicio 1

## Mostrar los números desde el 0 al número solicitado al usuario (input)

print('1. MOSTRAR NÚMEROS DEL 0 AL NÚMERO INGRESADO\n')

numero = int(input("Ingresá un número: "))

for i in range(numero + 1):
    print(f"{i}\n")
    
    
## Mostrar sólo los números pares desde 0 hasta el número ingresado (input)

print('2. MOSTRAR NÚMEROS PARES DESDE EL 0 AL NÚMERO INGRESADO\n')

numero = int(input("Ingresá un número: "))

for i in range(numero + 1):
    if i % 2 == 0:
        print(f"{i}\n")
        
## Pedir que el usuario ingrese nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

print('3. MOSTRAR NOMBRES HASTA INGRESAR "FIN"\n')

nombre = ""
while nombre.lower() != "fin":
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() != "fin":
        print(f"{nombre}\n")
        
## En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas de los alumnos de un curso.
# Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6).
# Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

print('4. PROMEDIO ESCOLAR\n')

cantidad_alumnos = int(input("Ingresá la cantidad de alumnos: "))
suma_notas = 0

for i in range(cantidad_alumnos):
    nota = float(input(f"Ingresá la nota del alumno {i+1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_alumnos

print(f"Promedio: {promedio}.")

if promedio > 8:
    print("El rendimiento ha sido elevado.\n")
elif promedio >= 6:
    print("El rendimiento ha sido aceptable.\n")
else:
    print("El rendimiento ha sido bajo.\n")
    

## Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10.

print("5. TABLA DE MULTIPLICAR - SOLUCIÓN MIENTRAS (while) \n")

numero = int(input("Ingresá un número entre 1 y 10: "))
i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}\n")
    i += 1
    
print("5. TABLA DE MULTIPLICAR - SOLUCIÓN PARA (for) \n")

numero = int(input("Ingresá un número entre 1 y 10: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}\n")