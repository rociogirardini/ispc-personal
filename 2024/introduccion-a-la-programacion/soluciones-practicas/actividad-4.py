# ---- Estructuras de Datos ---- 

### ACTIVIDAD PARTE 1

print('ACTIVIDAD - PARTE 1\n')

## Pedir al usuario que ingresá 10 nombres de personas no repetidas, guardarlos en una lista y mostrarlos. 

print('Ingresá 10 nombres diferentes. Una vez lo hayas hecho, los verás uno debajo del otro.\n')

nombres = []

while len(nombres) < 10:
    nombre = input(f"Ingresá el nombre {len(nombres) + 1}: ")
    if nombre in nombres:
        print(f"Ya habías ingresado {nombre} anteriormente. Intentá con otro nombre.")
    else:
        nombres.append(nombre)

print("Los 10 nombres ingresados son:")
for nombre in nombres:
    print(nombre)


## Eliminar la tercer y la última persona de la lista, ordenar y mostrar.

print('------------------\n')
print('Ahora, vas a ver la misma lista, solo que ordenada, y sin la tercer y la última persona.\n')

del nombres[2]
del nombres[-1]

nombres.sort()

print("Los nombres ordenados son:")
for nombre in nombres:
    print(nombre)
    
## Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento; y mostrar.

print('------------------\n')
print('Sigamos! Vamos a guardar tus datos en un diccionario.\n')

persona = {}
persona["nombre"] = input("Ingresá tu nombre: ")
persona["apellido"] = input("Ingresá tu apellido: ")
persona["dni"] = input("Ingresá tu DNI: ")
persona["email"] = input("Ingresá tu email: ")
persona["fecha_nacimiento"] = input("Ingresá la fecha de nacimiento: ")

print("Los datos ingresados son:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

## En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos.

print('------------------\n')
print('A continuación, ingresá los datos de familia:\n')

familia = {}

for i in range(4):
    persona = {}
    persona["nombre"] = input(f"Ingresá el nombre de la persona {i+1}: ")
    persona["apellido"] = input(f"Ingresá el apellido de la persona {i+1}: ")
    persona["dni"] = input(f"Ingresá el DNI de la persona {i+1}: ")
    persona["email"] = input(f"Ingresá el email de la persona {i+1}: ")
    persona["fecha_nacimiento"] = input(f"Ingresá la fecha de nacimiento de la persona {i+1}: ")
    familia[f"persona_{i+1}"] = persona


print("Los datos de la familia son:")
for i, (clave, valor) in enumerate(familia.items(), start=1):
    print(f"PERSONA {i}:")
    print(f"{clave}: {valor}\n")
    

## Guardar en una tupla los primeros n números pares. El valor de n que lo ingresá el usuario (input). Luego mostrar.

print('------------------\n')
print('Ahora veremos los primeros números pares según el valor que ingresás: \n')

n = int(input("Ingresá el valor de n: "))
numeros_pares = []
i = 1

while len(numeros_pares) < n:
    if i % 2 == 0:
        numeros_pares.append(i)
    i += 1

tupla_pares = tuple(numeros_pares)

print("Los primeros", n, "números pares son:")
print(tupla_pares)


### ACTIVIDAD PARTE 2

print('ACTIVIDAD - PARTE 2\n')

print('------------------\n')
print('En esta parte 2 vas a poder navegar por un menú para poder gestionar tu agenda de contactos: \n')

def gestionar_agenda():
    agenda = {} 

    # 1. Agregar una persona
    def agregar_persona():
        apellido = input("Ingresá el apellido: ")
        nombre = input("Ingresá el nombre: ")
        dni = input("Ingresá el DNI: ")
        email = input("Ingresá el email: ")
        telefono = input("Ingresá el número de teléfono: ")
        agenda[dni] = {"apellido": apellido, "nombre": nombre, "email": email, "telefono": telefono}
        print("Persona agregada correctamente.")

    # 2. Modificar los datos de una persona
    def modificar_persona():
        dni = input("Ingresá el DNI de la persona que querés modificar: ")
        if dni in agenda:
            print("Datos actuales:", agenda[dni])
            modificar = input("¿Desea modificar los datos de esta persona? (si/no): ")
            if modificar.lower() == "si":
                agenda[dni]["apellido"] = input("Ingresá el nuevo apellido (dejalo vacío para no modificar): ") or agenda[dni]["apellido"]
                agenda[dni]["nombre"] = input("Ingresá el nuevo nombre (dejalo vacío para no modificar): ") or agenda[dni]["nombre"]
                agenda[dni]["email"] = input("Ingresá el nuevo email (dejalo vacío para no modificar): ") or agenda[dni]["email"]
                agenda[dni]["telefono"] = input("Ingresá el nuevo número de teléfono (dejalo vacío para no modificar): ") or agenda[dni]["telefono"]
                print("Persona modificada correctamente.")
            else:
                print("No se han realizado modificaciones.")
        else:
            print("La persona con ese DNI no existe en la agenda.")

    # 3. Eliminar una persona de la agenda
    def eliminar_persona():
        dni = input("Ingresá el DNI de la persona que desea eliminar: ")
        if dni in agenda:
            del agenda[dni]
            print("Persona eliminada correctamente.")
        else:
            print("La persona con ese DNI no existe en la agenda.")

    # 4. Mostrar todos los contactos de la agenda
    def mostrar_agenda():
        print("Agenda telefónica:\n")
        for dni, datos in agenda.items():
            print("DNI:", dni)
            print("Apellido:", datos["apellido"])
            print("Nombre:", datos["nombre"])
            print("Email:", datos["email"])
            print("Teléfono:", datos["telefono"])
            print("-" * 20, "\n")

    # 5. Mostrar el menú de opciones
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar una persona")
        print("2. Modificar una persona")
        print("3. Eliminar una persona")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            modificar_persona()
        elif opcion == "3":
            eliminar_persona()
        elif opcion == "4":
            mostrar_agenda()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    gestionar_agenda()
