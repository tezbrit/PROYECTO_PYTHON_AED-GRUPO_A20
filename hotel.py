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