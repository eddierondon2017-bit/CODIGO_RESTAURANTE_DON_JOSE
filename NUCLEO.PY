import logica_de_restarante_don_jose
import almacenamiento_datos_de_mesa

# Nombre del archivo donde se guardan las reservas
ELARCHIVO = "reservas_don_jose.json"

def menu():
    # Muestra el menú principal y retorna la opción elegida
    print("========================================================================")
    print("--- Restaurante Don José ---")
    print("1. Agregar reserva")
    print("2. Modificar reserva")
    print("3. Eliminar reserva")
    print("4. Buscar reserva")
    print("5. Ver todas las reservas")
    print("6. Ver disponibilidad")
    print("7. Vaciar todas las reservas")
    print("8. Salir")
    print("========================================================================")
    return input("Seleccione una opción: ")

def inicio():
    # Carga las reservas guardadas al iniciar el programa
    reservas = almacenamiento_datos_de_mesa.cargar_datos_desde_archivo(ELARCHIVO)

    while True:
        opcion = menu()

        # --- OPCIÓN 1: Agregar nueva reserva ---
        if opcion == '1':
            # Repite hasta que el nombre no esté vacío
            while True:
                nombre = input("Ingrese el nombre del cliente para la reserva: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Intente de nuevo.")

            # Repite hasta que la cantidad sea un número mayor a cero
            while True:
                try:
                    cantidad_personas = int(input("Ingrese la cantidad de personas: "))
                    if cantidad_personas > 0:
                        break
                    print("La cantidad debe ser mayor a cero. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número válido. Intente de nuevo.")

            # Repite hasta que la hora no esté vacía
            while True:
                hora = input("Ingrese la hora de la reserva (ej. 19:00): ").strip()
                if hora:
                    break
                print("La hora no puede estar vacía. Intente de nuevo.")

            # Verifica disponibilidad y agrega la reserva
            exito, mensaje = logica_de_restarante_don_jose.verificacion_agregar_reserva(reservas, nombre, cantidad_personas, hora)
            print(mensaje)
            if exito:
                almacenamiento_datos_de_mesa.actualizar_datos_en_archivo(reservas, ELARCHIVO)

        # --- OPCIÓN 2: Modificar una reserva existente ---
        elif opcion == '2':
            # Repite hasta que el nombre no esté vacío
            while True:
                nombre = input("Ingrese el nombre de la reserva a modificar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Intente de nuevo.")

            # Repite hasta que el nuevo nombre no esté vacío
            while True:
                nuevo_nombre = input("Ingrese el nuevo nombre para la reserva: ").strip()
                if nuevo_nombre:
                    break
                print("El nuevo nombre no puede estar vacío. Intente de nuevo.")

            # Repite hasta que la nueva cantidad sea válida
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad de personas: "))
                    if nueva_cantidad > 0:
                        break
                    print("La cantidad debe ser mayor a cero. Intente de nuevo.")
                except ValueError:
                    print("Ingrese un número válido. Intente de nuevo.")

            # Repite hasta que la nueva hora no esté vacía
            while True:
                nueva_hora = input("Ingrese la nueva hora de la reserva (ej. 19:00): ").strip()
                if nueva_hora:
                    break
                print("La hora no puede estar vacía. Intente de nuevo.")

            # Aplica la modificación y guarda si fue exitosa
            exito, mensaje = logica_de_restarante_don_jose.modificar_reserva(reservas, nombre, nuevo_nombre, nueva_cantidad, nueva_hora)
            print(mensaje)
            if exito:
                almacenamiento_datos_de_mesa.actualizar_datos_en_archivo(reservas, ELARCHIVO)

        # --- OPCIÓN 3: Eliminar una reserva ---
        elif opcion == '3':
            # Repite hasta que el nombre no esté vacío
            while True:
                nombre = input("Ingrese el nombre de la reserva a eliminar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Intente de nuevo.")

            # Busca y elimina la reserva
            exito, mensaje = logica_de_restarante_don_jose.eliminar_reserva(reservas, nombre)
            print(mensaje)
            if exito:
                almacenamiento_datos_de_mesa.actualizar_datos_en_archivo(reservas, ELARCHIVO)

        # --- OPCIÓN 4: Buscar una reserva por nombre ---
        elif opcion == '4':
            # Repite hasta que el nombre no esté vacío
            while True:
                nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Intente de nuevo.")

            # Muestra los datos si encuentra la reserva
            resultado = logica_de_restarante_don_jose.buscar_reserva(reservas, nombre)
            if resultado:
                print("Reserva encontrada:")
                print(f"   Nombre  : {resultado['nombre']}")
                print(f"   Personas: {resultado['personas']}")
                print(f"   Hora    : {resultado['hora']}")
            else:
                print(f"No se encontró ninguna reserva para '{nombre}'.")

        # --- OPCIÓN 5: Ver todas las reservas activas ---
        elif opcion == '5':
            print(logica_de_restarante_don_jose.mostrar_reservas(reservas))

        # --- OPCIÓN 6: Ver disponibilidad actual ---
        elif opcion == '6':
            print(logica_de_restarante_don_jose.mostrar_disponibilidad(reservas))

        # --- OPCIÓN 7: Vaciar todas las reservas ---
        elif opcion == '7':
            # Primera confirmación
            confirmacion = input("⚠️⚠️⚠️⚠️⚠️⚠️ ¿Seguro que desea eliminar TODAS las reservas? (s/n): ⚠️⚠️⚠️⚠️⚠️ ").strip().lower()
            if confirmacion == "s":
                # Segunda confirmación para evitar borrados accidentales
                segurisimo = input("⚠️⚠️⚠️⚠️⚠️⚠️ Escriba 'CONFIRMAR' para proceder: ⚠️⚠️⚠️⚠️⚠️ ").strip().upper()
                if segurisimo == "CONFIRMAR":
                    mensaje = logica_de_restarante_don_jose.vaciar_todo(reservas)
                    print(mensaje)
                    almacenamiento_datos_de_mesa.actualizar_datos_en_archivo(reservas, ELARCHIVO)
                else:
                    print("Confirmación incorrecta. Operación cancelada.")
            else:
                print("Operación cancelada.")

        # --- OPCIÓN 8: Guardar y salir ---
        elif opcion == '8':
            almacenamiento_datos_de_mesa.guardar_datos_en_archivo(reservas, ELARCHIVO)
            print("Datos guardados. ¡Hasta mañana, Don José!")
            break

        # --- Opción no reconocida ---
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    inicio()
    
