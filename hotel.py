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

def cargar_huespedes():
    huespedes = []
    
    if not os.path.exists(ARCHIVO_HUESPEDES):
        return huespedes

    archivo = open(ARCHIVO_HUESPEDES, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")
            huesped = {
                "nombre":     partes[0],
                "dni":        partes[1],
                "habitacion": int(partes[2]),
                "noches":     int(partes[3]),
                "total":      int(partes[4])
            }
            huespedes.append(huesped)
    archivo.close()

    return huespedes


def guardar_huespedes(huespedes):
    archivo = open(ARCHIVO_HUESPEDES, "w", encoding="utf-8")
    for h in huespedes:
        linea = h["nombre"] + "," + h["dni"] + "," + str(h["habitacion"]) + "," + str(h["noches"]) + "," + str(h["total"]) + "\n"
        archivo.write(linea)
    archivo.close()

def mostrar_menu():
    print("")
    print("=" * 40)
    print("   SISTEMA DE GESTION DE HOTEL")
    print("=" * 40)
    print("  1. Ver habitaciones disponibles")
    print("  2. Registrar huesped (Check-in)")
    print("  3. Realizar Check-out")
    print("  4. Ver huespedes actuales")
    print("  5. Ver estadisticas del hotel")
    print("  6. Salir")
    print("=" * 40)

def ver_habitaciones_disponibles(habitaciones):
    print("")
    print("=== Habitaciones disponibles ===")

    disponibles = 0
    
    for hab in habitaciones:
        if hab["estado"] == "disponible":
            print("Habitacion " + str(hab["numero"]) + " | " + hab["tipo"] + " | $" + str(hab["precio"]) + " por noche")
            disponibles += 1

    if disponibles == 0:
        print("No hay habitaciones disponibles en este momento.")
    else:
        print("Total disponibles: " + str(disponibles))

def registrar_huesped(habitaciones, huespedes):
    print("")
    print("=== Registro de huesped (Check-in) ===")

    hay_disponibles = False
    for hab in habitaciones:
        if hab["estado"] == "disponible":
            hay_disponibles = True
            break

    if not hay_disponibles:
        print("No hay habitaciones disponibles en este momento.")
        return

    nombre = input("Nombre completo del huesped: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    dni = ""
    while True:
        dni = input("DNI del huesped: ").strip()
        if dni.isdigit() and len(dni) >= 7:
            break
        print("DNI invalido. Ingresa solo numeros (minimo 7 digitos).")

    for h in huespedes:
        if h["dni"] == dni:
            print("Ese DNI ya tiene una reserva activa.")
            return


    print("")
    print("Tipos de habitacion:")
    print("  1. Simple  - $15000 por noche")
    print("  2. Doble   - $25000 por noche")
    print("  3. Suite   - $45000 por noche")

    tipo_elegido = ""
    while True:
        opcion_tipo = input("Elegi el tipo (1/2/3): ").strip()
        if opcion_tipo == "1":
            tipo_elegido = "Simple"
            break
        elif opcion_tipo == "2":
            tipo_elegido = "Doble"
            break
        elif opcion_tipo == "3":
            tipo_elegido = "Suite"
            break
        else:
            print("Opcion invalida. Elegi 1, 2 o 3.")


    habitacion_asignada = None
    for hab in habitaciones:
        if hab["tipo"] == tipo_elegido and hab["estado"] == "disponible":
            habitacion_asignada = hab
            break

    if habitacion_asignada is None:
        print("No hay habitaciones de tipo " + tipo_elegido + " disponibles en este momento")
        return


    noches = 0
    while noches <= 0:
        noches_str = input("Cantidad de noches: ").strip()
        if noches_str.isdigit():
            noches = int(noches_str)
            if noches <= 0:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Ingresa un número válido")


    total = habitacion_asignada["precio"] * noches

    # Marcar habitación como ocupada
    habitacion_asignada["estado"] = "ocupada"
    habitacion_asignada["dni"]    = dni


    nuevo_huesped = {
        "nombre":     nombre,
        "dni":        dni,
        "habitacion": habitacion_asignada["numero"],
        "noches":     noches,
        "total":      total
    }
    huespedes.append(nuevo_huesped)

    guardar_habitaciones(habitaciones)
    guardar_huespedes(huespedes)

    print("")
    print("Check-in realizado con exito")
    print("Huesped:    " + nombre)
    print("DNI:        " + dni)
    print("Habitacion: " + str(habitacion_asignada["numero"]) + " (" + tipo_elegido + ")")
    print("Noches:     " + str(noches))
    print("Total:      $" + str(total))

def hacer_checkout(habitaciones, huespedes):
    print("")
    print("=== Check-out ===")

    if len(huespedes) == 0:
        print("No hay huespedes registrados actualmente.")
        return

    dni = input("Ingresa el DNI del huesped: ").strip()

    huesped_encontrado = None
    for h in huespedes:
        if h["dni"] == dni:
            huesped_encontrado = h
            break

    if huesped_encontrado is None:
        print("No se encontro ningun huesped con ese DNI.")
        return

    print("")
    print("Huesped:    " + huesped_encontrado["nombre"])
    print("Habitacion: " + str(huesped_encontrado["habitacion"]))
    print("Noches:     " + str(huesped_encontrado["noches"]))
    print("Total:      $" + str(huesped_encontrado["total"]))

    confirmacion = input("Confirmar check-out? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Check-out cancelado.")
        return

    for hab in habitaciones:
        if hab["numero"] == huesped_encontrado["habitacion"]:
            hab["estado"] = "disponible"
            hab["dni"]    = ""
            break

    huespedes.remove(huesped_encontrado)

    guardar_habitaciones(habitaciones)
    guardar_huespedes(huespedes)

    print("Check-out realizado. Hasta la proxima, " + huesped_encontrado["nombre"] + "!")

def ver_huespedes_actuales(huespedes):
    print("")
    print("=== Huespedes actuales ===")

    if len(huespedes) == 0:
        print("No hay huespedes registrados actualmente.")
        return

    for h in huespedes:
        print("- " + h["nombre"] + " | DNI: " + h["dni"] + " | Hab: " + str(h["habitacion"]) + " | Noches: " + str(h["noches"]) + " | Total: $" + str(h["total"]))

    print("Total de huespedes: " + str(len(huespedes)))

def ver_estadisticas(habitaciones, huespedes):
    print("")
    print("=== Estadisticas del hotel ===")

    total_simple    = 0
    total_doble     = 0
    total_suite     = 0
    ocupadas_simple = 0
    ocupadas_doble  = 0
    ocupadas_suite  = 0
    recaudacion     = 0  

    for hab in habitaciones:
        if hab["tipo"] == "Simple":
            total_simple += 1
            if hab["estado"] == "ocupada":
                ocupadas_simple += 1
        elif hab["tipo"] == "Doble":
            total_doble += 1
            if hab["estado"] == "ocupada":
                ocupadas_doble += 1
        elif hab["tipo"] == "Suite":
            total_suite += 1
            if hab["estado"] == "ocupada":
                ocupadas_suite += 1

    for h in huespedes:
        recaudacion += h["total"]

    total_ocupadas   = ocupadas_simple + ocupadas_doble + ocupadas_suite
    total_disponibles = len(habitaciones) - total_ocupadas

    print("Total de habitaciones: " + str(len(habitaciones)))
    print("Ocupadas:              " + str(total_ocupadas))
    print("Disponibles:           " + str(total_disponibles))
    print("")
    print("Simple -> " + str(ocupadas_simple) + "/" + str(total_simple) + " ocupadas")
    print("Doble  -> " + str(ocupadas_doble)  + "/" + str(total_doble)  + " ocupadas")
    print("Suite  -> " + str(ocupadas_suite)  + "/" + str(total_suite)  + " ocupadas")
    print("")
    print("Recaudacion actual: $" + str(recaudacion))
    print("Huespedes actuales: " + str(len(huespedes)))


    if total_ocupadas > 0:
        tipo_mas_solicitado = "Simple"
        max_ocupadas = ocupadas_simple

        if ocupadas_doble > max_ocupadas:
            max_ocupadas = ocupadas_doble
            tipo_mas_solicitado = "Doble"

        if ocupadas_suite > max_ocupadas:
            tipo_mas_solicitado = "Suite"

        print("Tipo mas solicitado: " + tipo_mas_solicitado)

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