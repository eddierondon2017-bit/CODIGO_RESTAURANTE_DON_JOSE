import json
import os

def guardar_datos_en_archivo(datos, nombre_archivo):
    """Guarda los datos en un archivo JSON."""
    with open(nombre_archivo, 'w', encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos_desde_archivo(nombre_archivo):
    """Carga los datos desde un archivo JSON. Si el archivo no existe, devuelve una lista vacía."""
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            return json.load(archivo)
    else:
        return []

def eliminar_archivo(nombre_archivo):
    """Elimina el archivo si existe."""
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)

def actualizar_datos_en_archivo(datos, nombre_archivo):
    """Actualiza los datos en el archivo JSON."""
    eliminar_archivo(nombre_archivo)
    guardar_datos_en_archivo(datos, nombre_archivo)