# PaisPedia

## Trabajo Práctico Integrador – Programación I

### Tecnicatura Universitaria en Programación


## Integrantes

- Borquez Kasem Francisco Aron
- Palacio Nicolas ivan

## Descripción del proyecto

PaisPedia es una aplicación desarrollada en Python que permite gestionar información sobre distintos países utilizando un archivo CSV como fuente de datos.

El sistema ofrece un menú interactivo mediante el cual el usuario puede realizar diferentes operaciones sobre el conjunto de datos, tales como agregar nuevos países, actualizar información existente, realizar búsquedas y aplicar filtros.

Este proyecto fue desarrollado con el objetivo de aplicar los contenidos trabajados durante la asignatura Programación I, haciendo uso de listas, diccionarios, funciones, estructuras condicionales y repetitivas, lectura de archivos CSV y validaciones de datos.

---

## Funcionalidades

- Agregar un nuevo país.
- Actualizar la población y la superficie de un país.
- Buscar un país por nombre.
- Filtrar países por continente.
- Filtrar países por rango de población.
- Filtrar países por rango de superficie.
- Validación de datos ingresados.
- Manejo de errores mediante `try` y `except`.



## Requisitos

- Python 3.12 o superior.
- Archivo `Paises.csv` ubicado en la misma carpeta que el programa.



## Ejecución

1. Descargar o clonar el repositorio.

```bash
git clone https://github.com/USUARIO/PaisPedia.git
```

2. Ingresar a la carpeta del proyecto.

```bash
cd PaisPedia
```

3. Ejecutar el programa.

```bash
python TPI_Programacion.py
```


## Estructura del proyecto


PaisPedia/
│
├── TPI_Programacion.py
├── Paises.csv
├── README.md
└── Documentacion.pdf


## Ejemplo de uso

### Menú principal


~~~ Bienvenidos a PaisPedia ~~~

1) Agregar un país
2) Actualizar población y superficie
3) Buscar un país
4) Filtrar países
5) Ordenar países
6) Mostrar estadísticas
7) Salir
```

### Ejemplo de búsqueda

**Entrada**


Ingrese el nombre del país:
Argentina

**Salida**


El país Argentina tiene una población de 45.376.763 habitantes,
una superficie de 2.780.400 km²
y pertenece al continente América.




## Validaciones implementadas

El programa verifica:

- Campos obligatorios.
- Nombres vacíos.
- Países duplicados.
- Valores numéricos válidos.
- Valores positivos para población y superficie.
- Rangos de filtros correctos.

En caso de producirse un error de ingreso, el sistema muestra un mensaje descriptivo y solicita nuevamente el dato.



## Documentación

 Informe en PDF



## Video demostrativo

 Enlace al video:



## Repositorio

https://github.com/USUARIO/PaisPedia

