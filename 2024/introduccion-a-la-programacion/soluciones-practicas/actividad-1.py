# ---- Estructura Secuencial ---- 

## Ejercicio 1

# Un estudiante está cursando 5 materias, tiene la nota de cada materia y quiere saber cuál es su promedio.

print(f"EJERCICIO 1\n")

nota1 = float(input("Introduce la nota de la materia 1: "))
nota2 = float(input("Introduce la nota de la materia 2: "))
nota3 = float(input("Introduce la nota de la materia 3: "))
nota4 = float(input("Introduce la nota de la materia 4: "))
nota5 = float(input("Introduce la nota de la materia 5: "))

suma_notas = nota1, nota2, nota3, nota4, nota5

promedio = sum(suma_notas) / 5

print(f"El promedio de las notas es: {promedio:.2f}\n")

## Ejercicio 2

# Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar.
# El cliente le indica que necesita conocer el costo de mano de obra para pintar una pared rectangular de un galpón.
# El pintor cobra un monto ﬁjo por cada metro cuadrado.
# Hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.

print(f"EJERCICIO 2\n")

ancho = float(input("Ingrese el ancho de la pared en metros: "))
alto = float(input("Ingrese el alto de la pared en metros: "))
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado: "))

area_pared = ancho * alto

costo_total = area_pared * costo_por_metro_cuadrado

print(f"El costo total para pintar la pared es: ${costo_total:.2f}\n")

## Ejercicio 3

# Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato.
# Para ello recibe cada semana la información de la cantidad total de partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado.
# Por cada partido empatado recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

print(f"EJERCICIO 3\n")

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados * 1
puntos_perdidos = partidos_perdidos * 0  # Este cálculo no hace falta, pero lo agrego para que quede más prolijo todo

puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos

print(f"El equipo ha acumulado un total de {puntos_totales} puntos.\n")