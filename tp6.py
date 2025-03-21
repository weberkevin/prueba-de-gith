"""1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
notas, cantidad de faltas, cantidad de amonestaciones recibidas.
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos"""

datos = {"Alumnos": []}
def mostrar_alumnos():
    for i in range(len(datos["Alumnos"])):
        alumno = datos["Alumnos"][i]
        print(f"{i + 1}. {alumno['Nombre']} {alumno['Apellido']} (DNI: {alumno['DNI']})")
def mostrar_datos_alumno():
    mostrar_alumnos()
    indice = int(input("Ingrese el número del alumno: ")) - 1
    alumno = datos["Alumnos"][indice]
    for clave in alumno:
        print(f"{clave}: {alumno[clave]}")
def modificar_alumno():
    mostrar_alumnos()
    indice = int(input("Ingrese el número del alumno a modificar: ")) - 1
    alumno = datos["Alumnos"][indice]
    campos = alumno()
    print("Campos disponibles:", campos)
    campo = input("Ingrese el campo a modificar: ")
    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
    if campo in ["Notas", "Faltas", "Amonestaciones"]:
        nuevo_valor = int(nuevo_valor)
    alumno[campo] = nuevo_valor
    print("Datos actualizados correctamente.")
def agregar_alumno():
    nuevo_alumno = {
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "DNI": input("DNI: "),
        "Fecha de nacimiento": input("Fecha de nacimiento: "),
        "Tutor": input("Nombre del Tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0}
    datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado correctamente.")
def expulsar_alumno():
    mostrar_alumnos()
    indice = int(input("Ingrese el número del alumno a expulsar: ")) - 1
    datos["Alumnos"].pop(indice)
    print("Alumno expulsado correctamente.")
def menu():
    while True:
        print("Menú:")
        print("1. Mostrar alumnos")
        print("2. Ver datos de un alumno")
        print("3. Modificar datos de un alumno")
        print("4. Agregar alumno")
        print("5. Expulsar alumno")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_alumnos()
        if opcion == "2":
            mostrar_datos_alumno()
        if opcion == "3":
            modificar_alumno()
        if opcion == "4":
            agregar_alumno()
        if opcion == "5":
            expulsar_alumno()
        if opcion == "6":
            print("Saliendo del programa...")
            break
menu()