# ---- Estructura Condicional ---- 

### Ejercicio 1

## Condicional parcial (solo el if) con expresión lógica simple

# Verificar si una persona es mayor de edad. Si lo es, se imprime un mensaje indicando que la persona es mayor de edad.

print("1. CONDICIONAL PARCIAL CON EXPRESIÓN LÓGICA SIMPLE.\n")

edad = int(input("Ingresá tu edad: "))

if edad >= 18:
    print("Sos mayor de edad.\n")
    
    
## Condicional completo (if - else) con expresión lógica simple

# Verificar si un número es par o impar. Si es par, se imprime un mensaje indicando que el número es par. Si no, se imprime un mensaje indicando que el número es impar.

print("2. CONDICIONAL COMPLETO CON EXPRESIÓN LÓGICA SIMPLE.\n")

numero = int(input("Ingresá un número: "))

if numero % 2 == 0:
    print("El número es par.\n")
else:
    print("El número es impar.\n")
    
## Condicional parcial (solo if) con expresión lógica compuesta (and)

# Verificar si una persona está dentro del rango etario laboral (entre 18 y 60 años inclusive). Si lo es, se imprime un mensaje indicando que la persona es apta para trabajar.

print("3. CONDICIONAL PARCIAL CON EXPRESIÓN LÓGICA COMPUESTA.\n")

edad = int(input("Ingresá tu edad: "))

if edad >= 18 and edad <= 60:
    print("Estás apto para trabajar.\n")



## Condicional completo (if - else) con expresión lógica compuesta (or)

# Verificar si una persona es un niño o un adulto mayor. Si la edad es menor a 12 años o mayor a 60 años, se imprime un mensaje indicando que la persona es un niño o un adulto mayor. Si no, se imprime un mensaje indicando que la persona es un adulto.

print("4. CONDICIONAL COMPLETO CON EXPRESIÓN LÓGICA COMPUESTA.\n")

edad = int(input("Ingresá tu edad: "))

if edad < 12 or edad > 60:
    print("Sos un niño o un adulto mayor.\n")
else:
    print("Sos un adulto.\n")
    


## Ejemplo de la despensa

# Una despensa vende leche a 1000 pesos por litro.
# Si un cliente compra más de 12 unidades, obtiene un descuento del 10%.
# Si compra más de 24 unidades, obtiene un descuento del 15%. Además, los jubilados obtienen un 10% de descuento adicional, acumulable con los anteriores descuentos.
# El algoritmo calculará el costo total considerando los descuentos.

print("5. EJEMPLO DE LA DESPENSA.\n")

precio_leche = 1000

cantidad = int(input("Ingresá la cantidad de litros de leche: "))
es_jubilado = input("¿Sos jubilado? (si/no): ").strip().lower()

descuento = 0

if cantidad > 24:
    descuento = 15
elif cantidad > 12:
    descuento = 10

if es_jubilado == "si":
    descuento += 10

costo_bruto = cantidad * precio_leche
descuento_total = costo_bruto * (descuento / 100)
costo_final = costo_bruto - descuento_total

print(f"El costo total a pagar es: ${costo_final:.2f}\n")
