# LA CAPACIDAD DEL RESTAURANTE ES DE 100 PERSONAS
CAPACIDAD_MAXIMA = 100

def obtener_ocupacion_total(reservas):
    """Suma las reservas totales del restaurante activas."""
    return sum(reserva['personas'] for reserva in reservas)

def verificacion_agregar_reserva(reservas, nombre, cantidad_personas, hora):
    """Verifica si se puede agregar una nueva reserva sin sobrepasar la capacidad máxima."""
    ocupacion_total = obtener_ocupacion_total(reservas)
    if ocupacion_total + cantidad_personas <= CAPACIDAD_MAXIMA:
        reservas.append({
            "nombre": nombre,
            "personas": cantidad_personas,
            "hora": hora
        })
        return True, f"Reserva agregada exitosamente para {nombre} a las {hora}."
    else:
        disponibilidad = CAPACIDAD_MAXIMA - ocupacion_total
        return False, f"No se puede agregar la reserva. Disponibilidad actual: {disponibilidad} personas."

def buscar_reserva(reservas, nombre):
    """Busca una reserva por nombre y devuelve su información."""
    for reserva in reservas:
        if reserva['nombre'].lower() == nombre.lower():
            return reserva
    return None

def modificar_reserva(reservas, nombre, nuevo_nombre, nueva_cantidad, nueva_hora):
    """Modifica una reserva existente si se encuentra y no sobrepasa la capacidad máxima."""
    reserva = buscar_reserva(reservas, nombre)
    if reserva:
        ocupacion_sin_esta = obtener_ocupacion_total(reservas) - reserva['personas']
        if ocupacion_sin_esta + nueva_cantidad <= CAPACIDAD_MAXIMA:
            reserva['nombre'] = nuevo_nombre
            reserva['personas'] = nueva_cantidad
            reserva['hora'] = nueva_hora
            return True, f"Reserva modificada exitosamente para {nuevo_nombre}."
        else:
            disponibilidad = CAPACIDAD_MAXIMA - ocupacion_sin_esta
            return False, f"No se puede modificar. Disponibilidad actual: {disponibilidad} personas."
    else:
        return False, f"No se encontró una reserva para '{nombre}'."

def eliminar_reserva(reservas, nombre):
    """Elimina una reserva por nombre si se encuentra."""
    for i, reserva in enumerate(reservas):
        if reserva['nombre'].lower() == nombre.lower():
            del reservas[i]
            return True, f"Reserva eliminada exitosamente para {nombre}."
    return False, f"No se encontró una reserva para '{nombre}'."

def mostrar_reservas(reservas):
    """Muestra todas las reservas activas."""
    if reservas:
        return "\n".join([f"{r['nombre']} - {r['personas']} personas - {r['hora']}" for r in reservas])
    else:
        return "No hay reservas activas."

def mostrar_disponibilidad(reservas):
    """Muestra la disponibilidad actual del restaurante."""
    ocupacion_total = obtener_ocupacion_total(reservas)
    disponibilidad = CAPACIDAD_MAXIMA - ocupacion_total
    return f"Capacidad máxima: {CAPACIDAD_MAXIMA} | Ocupación actual: {ocupacion_total} | Disponibilidad: {disponibilidad} personas."

def vaciar_todo(reservas):
    """Elimina todas las reservas activas."""
    reservas.clear()
    return "Todas las reservas han sido eliminadas."
