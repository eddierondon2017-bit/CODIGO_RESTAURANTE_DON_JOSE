# CODIGO_RESTAURANTE_DON_JOSE
Repositorio que se encarga de almacenar el proyecto del curso "Python 0-100" de ACM-UD
# Sistema de Reservas - Restaurante Don José
Aplicación de consola desarrollada en Python para la gestión de reservas de un restaurante.
Este sistema permite registrar, modificar, buscar y eliminar reservas de clientes,
controlando automáticamente la capacidad máxima del restaurante y persistiendo
los datos en un archivo JSON para que no se pierdan al cerrar el programa.

El proyecto fue desarrollado como solución al problema planteado por Don José,
quien necesitaba digitalizar el control de reservas de su restaurante, reemplazando
el uso de papel y lápiz por un sistema que verificara disponibilidad, permitiera
modificar o cancelar reservas y conservara los datos entre sesiones.

# EL_UNICO_INTEGRANTE
Eddie santiago rondon capera 

# CODIGO
1026561145

# Características principales
La aplicación permite:
- Registrar nuevas reservas con nombre, cantidad de personas y hora
- Verificar automáticamente si hay cupo disponible antes de confirmar
- Buscar una reserva específica por nombre del cliente
- Modificar los datos de una reserva existente
- Eliminar reservas individuales
- Ver todas las reservas activas y la ocupación total
- Vaciar todas las reservas con doble confirmación de seguridad
- Guardar los datos automáticamente tras cada operación

#Estructura del proyecto
proyecto_restaurante_don_jose/
│
├── reservas_don_jose.json
│
├── logica_de_restarante_don_jose.py
├── almacenamiento_datos_de_mesa.py
├── nucleo.py
└── README.md

# Descripción de archivos

logica_de_restarante_don_jose.py
Módulo central de lógica de negocio. Contiene las siguientes funciones:
- Verificación de capacidad antes de agregar una reserva
- Búsqueda de reservas por nombre
- Modificación de reservas existentes
- Eliminación de reservas individuales
- Visualización de reservas activas y disponibilidad
- Vaciado completo de reservas

# almacenamiento_datos_de_mesa.py
Módulo responsable de la persistencia de datos. Gestiona:
- Carga de reservas desde el archivo JSON al iniciar
- Guardado de reservas tras cada operación
- Actualización y eliminación del archivo

# nucleo.py
Punto de entrada de la aplicación. Implementa el menú interactivo
que conecta la interfaz de consola con la lógica y el almacenamiento.

# reservas_don_jose.json
Archivo generado automáticamente donde se almacenan las reservas
en formato JSON. Se crea al registrar la primera reserva.

# Requisitos del sistema
- Python 3.10 o superior
- Sistemas operativos: Windows, Linux o macOS
- No requiere librerías externas (solo módulos estándar: json, os)

# Ejecución
Para iniciar la aplicación:
    python nucleo.py

Uso de la aplicación

Opción 1 - Agregar reserva
Ingrese el nombre del cliente, cantidad de personas y hora.
El sistema verificará automáticamente si hay cupo disponible.

Opción 2 - Modificar reserva
Busque la reserva por nombre e ingrese los nuevos datos.
El sistema valida que la nueva cantidad no supere la capacidad.

Opción 3 - Eliminar reserva
Ingrese el nombre del cliente y la reserva será eliminada.

Opción 4 - Buscar reserva
Ingrese el nombre del cliente para ver sus datos de reserva.

Opción 5 - Ver todas las reservas
Muestra la lista completa de reservas activas.

Opción 6 - Ver disponibilidad
Muestra la ocupación actual y los lugares disponibles.

Opción 7 - Vaciar todas las reservas
Elimina todas las reservas con doble confirmación de seguridad.

Opción 8 - Salir
Guarda los datos y cierra el programa.

# Tecnologías utilizadas
- Python: Lenguaje principal
- JSON: Almacenamiento de datos
- Módulo os: Gestión de archivos
- Módulo json: Serialización de datos

# Objetivo académico
Este proyecto fue desarrollado como solución para la materia Python de 0 a 100,
con el objetivo de aplicar conceptos de:
- Programación modular
- Manejo de archivos
- Estructuras de datos
- Validación de entradas
- Persistencia de información

# Posibles mejoras futuras
- Interfaz gráfica con Tkinter
- Filtros por hora o fecha
- Exportación de reportes en PDF
- Registro de historial de reservas canceladas
- Autenticación con contraseña para vaciar reservas

Autor
Proyecto desarrollado por Eddie Santiago Rondon Capera
Estudiante de ingenieria de sistemas
Universidad Distrital Francisco José de Caldas
