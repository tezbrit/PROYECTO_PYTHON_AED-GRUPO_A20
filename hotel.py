import os

ARCHIVO_HABITACIONES = "habitaciones.txt"
ARCHIVO_HUESPEDES    = "huespedes.txt"

def habitaciones_por_defecto():
    return [
        {"numero": 101, "tipo": "Simple", "precio": 45000, "estado": "disponible", "dni": ""},
        {"numero": 102, "tipo": "Simple", "precio": 45000, "estado": "disponible", "dni": ""},
        {"numero": 103, "tipo": "Simple", "precio": 45000, "estado": "disponible", "dni": ""},
        {"numero": 201, "tipo": "Doble",  "precio": 85000, "estado": "disponible", "dni": ""},
        {"numero": 202, "tipo": "Doble",  "precio": 85000, "estado": "disponible", "dni": ""},
        {"numero": 203, "tipo": "Doble",  "precio": 85000, "estado": "disponible", "dni": ""},
        {"numero": 301, "tipo": "Suite",  "precio": 100000, "estado": "disponible", "dni": ""},
        {"numero": 302, "tipo": "Suite",  "precio": 100000, "estado": "disponible", "dni": ""},
    ]

def cargar_habitaciones():
    habitaciones = []

    # Si el archivo no existe, es la primera vez que se abre el sistema
    if not os.path.exists(ARCHIVO_HABITACIONES):
        habitaciones = habitaciones_por_defecto()
        guardar_habitaciones(habitaciones)
        return habitaciones

    # Si el archivo existe, leemos línea por línea
    archivo = open(ARCHIVO_HABITACIONES, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")
            habitacion = {
                "numero": int(partes[0]),
                "tipo":   partes[1],
                "precio": int(partes[2]),
                "estado": partes[3],
                "dni":    partes[4]
            }
            habitaciones.append(habitacion)
    archivo.close()

    return habitaciones

def guardar_habitaciones(habitaciones):
    archivo = open(ARCHIVO_HABITACIONES, "w", encoding="utf-8")
    for h in habitaciones:
        linea = str(h["numero"]) + "," + h["tipo"] + "," + str(h["precio"]) + "," + h["estado"] + "," + h["dni"] + "\n"
        archivo.write(linea)
    archivo.close()

def main():
    print("Bienvenido al Sistema de Gestion de Hotel!")

    habitaciones = cargar_habitaciones()
    huespedes    = cargar_huespedes()

    while True:
        mostrar_menu()
        opcion = input("Elegi una opcion: ").strip()

        if opcion == "1":
            ver_habitaciones_disponibles(habitaciones)
        elif opcion == "2":
            registrar_huesped(habitaciones, huespedes)
        elif opcion == "3":
            hacer_checkout(habitaciones, huespedes)
        elif opcion == "4":
            ver_huespedes_actuales(huespedes)
        elif opcion == "5":
            ver_estadisticas(habitaciones, huespedes)
        elif opcion == "6":
            print("Hasta luego!")
            break
        else:
            print("Opcion invalida. Elegi un numero entre 1 y 6.")


main()