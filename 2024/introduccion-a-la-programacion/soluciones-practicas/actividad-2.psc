
# Condicional parcial (solo el if) con expresión lógica simple

INICIO
    Definir edad Como Entero

    Escribir "Ingresá tu edad: "
    Leer edad

    Si edad >= 18 Entonces
        Escribir "Sos mayor de edad."
    FinSi
FIN


# Condicional completo (if - else) con expresión lógica simple

INICIO
    Definir numero Como Entero

    Escribir "Ingresá un número: "
    Leer numero

    Si numero % 2 == 0 Entonces
        Escribir "El número es par."
    Sino
        Escribir "El número es impar."
    FinSi
FIN


# Condicional parcial (solo if) con expresión lógica compuesta (and)

INICIO
    Definir edad Como Entero

    Escribir "Ingresá tu edad: "
    Leer edad

    Si edad >= 18 y edad <= 60 Entonces
        Escribir "Sos apto para trabajar."
    FinSi
FIN

# Condicional completo (if - else) con expresión lógica compuesta (or)

INICIO
    Definir edad Como Entero

    Escribir "Ingrese su edad: "
    Leer edad

    Si edad < 12 o edad > 60 Entonces
        Escribir "Eres un niño o un adulto mayor."
    Sino
        Escribir "Eres un adulto."
    FinSi
FIN


# Ejemplo de la despensa

INICIO
    Definir precio_leche, cantidad, descuento, descuento_total, costo_bruto, costo_final Como Real
    Definir es_jubilado Como Cadena

    precio_leche <- 1000

    Escribir "Ingrese la cantidad de litros de leche: "
    Leer cantidad

    Escribir "¿Es usted jubilado? (si/no): "
    Leer es_jubilado

    descuento <- 0

    Si cantidad > 24 Entonces
        descuento <- 15
    Sino
        Si cantidad > 12 Entonces
            descuento <- 10
        FinSi
    FinSi

    Si es_jubilado = "si" Entonces
        descuento <- descuento + 10
    FinSi

    costo_bruto <- cantidad * precio_leche
    descuento_total <- costo_bruto * (descuento / 100)
    costo_final <- costo_bruto - descuento_total

    Escribir "El costo total a pagar es: $", costo_final

FIN
