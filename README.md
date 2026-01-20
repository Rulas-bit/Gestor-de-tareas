# Nombre del Proyecto
Teasker App
## Descripción
Este es mi primer proyecto en python, una aplicación de consola para gestionar tareas. Permite crear, listar, borrar e importar tareas desde un archivo JSON. 
He creado este proyecto para aprender a manejar archivos y estructuras de datos en Python, tambienpara practicar los conceptos básicos de programación orientada a objetos y manejo de excepciones.
y desarrollo de sowftware en general. pero sobre todo para aprender a programar mejor en python. 

## Instalación
1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio en tu máquina local usando: 
    ```bash
    git clone https://github.com/raulvaquero/teasker.git


## Uso
Aquí explico cómo usar el proyecto paso a paso.

1. Al ejecutar el programa, se mostrará un menú con opciones numeradas.
2. Ingresa el número correspondiente a la acción que deseas realizar (crear tarea, listar tareas, borrar tarea, importar tareas, guardar tareas o salir).
3. Sigue las instrucciones en pantalla para completar la acción seleccionada.
4. Para crear una tarea, añade el título y el estado cuando se te solicite.
5. Para listar tareas, simplemente selecciona la opción de listar y se mostrarán todas las tareas actuales.
6. Para borrar una tarea, ingresa el ID de la tarea que deseas eliminar.
7. Para importar tareas, proporciona el nombre del archivo JSON desde el cual deseas importar.
8. Para guardar tareas, proporciona el nombre del archivo JSON donde deseas guardar las tareas actuales.
## Estructura del Proyecto
├─ tasker.py
├─ data/
│  └─ tasks.json
├─ tests/
│  └─ test_tasker.py
├─ README.md
- tasker.py: Archivo principal que contiene la lógica de la aplicación.
- data/: Carpeta que contiene archivos de datos, como tareas guardadas en formato JSON.
- tests/: Carpeta que contiene pruebas unitarias para el proyecto.


- README.md: Este archivo de documentación del proyecto.

## Tecnologías usadas
- python
- unittest
- json

## Autor
Raúl Vaquero Pérez

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Para  qué sirve este proyecto
Este proyecto sirve como una herramienta básica de gestión de tareas para usuarios que prefieren trabajar en la consola. Permite a los usuarios organizar sus tareas diarias, mantener un seguimiento de las mismas y guardar su progreso en archivos JSON para futuras referencias.

## PAra que sirve cada archivo y como se utiliza
- tasker.py: Es el archivo principal que contiene la lógica de la aplicación. Aquí es donde se definen las funciones para crear, listar, borrar, importar y guardar tareas. También maneja la interacción con el usuario a través del menú de opciones.
- crear.py: Contiene la función para crear nuevas tareas. Solicita al usuario el título y el estado de la tarea, y la añade a la lista de tareas.
- listar.py: Contiene la función para listar todas las tareas actuales. Muestra cada tarea con su ID, título y estado.
- borrar.py: Contiene la función para borrar tareas. Solicita al usuario el ID de la tarea que desea eliminar y la elimina de la lista.
- marcar.py: Contiene la función para marcar tareas como completadas. Muestra las tareas disponibles y permite al usuario seleccionar una para cambiar su estado a "completada".
- importar.py: Contiene la función para importar tareas desde un archivo JSON. Lee el archivo y añade las tareas a la lista actual.
- guardar.py: Contiene la función para guardar las tareas actuales en un archivo JSON. Escribe la lista de tareas en el archivo especificado.
- menu.py: Contiene la función para mostrar el menú de opciones al usuario. Devuelve una cadena con las opciones disponibles.
- tests/: Esta carpeta contiene pruebas unitarias para cada una de las funcionalidades del proyecto. Cada archivo de prueba verifica que las funciones correspondientes en los otros archivos funcionen correctamente.
- test-menu.py: Prueba la función del menú para asegurarse de que todas las opciones estén presentes.
- test-crear.py: Prueba la función de creación de tareas.
- test-listar.py: Prueba la función de listado de tareas.
- test-borrar.py: Prueba la función de borrado de tareas.
- test-marcar.py: Prueba la función de marcar tareas como completadas.
- test-importar.py: Prueba la función de importación de tareas desde un archivo JSON.
- test-guardar.py: Prueba la función de guardado de tareas en un archivo JSON. Cada archivo de prueba utiliza la biblioteca unittest para definir casos de prueba y verificar que las funciones se comport

## Ejemplos de uso
1. Crear una tarea:
    - Selecciona la opción "1. Crear tarea" en el menú.
    - Ingresa el título de la tarea cuando se te solicite.
    - Ingresa el estado de la tarea (pendiente/completada).
2. Listar tareas:
    - Selecciona la opción "2. Listar tareas" en el menú.
    - Se mostrarán todas las tareas con sus detalles.
3. Borrar una tarea:
    - Selecciona la opción "4. Borrar tarea" en el menú.
    - Ingresa el ID de la tarea que deseas eliminar.
4. Marcar una tarea como completada:
    - Selecciona la opción "3. Marcar tarea como completada" en el menú.
    - Ingresa el número de la tarea que deseas marcar como completada.
5. Importar tareas desde un archivo JSON:
    - Selecciona la opción "8. Importar tareas" en el menú.
    - Ingresa el nombre del archivo JSON desde el cual deseas importar las tareas.
6. Guardar tareas en un archivo JSON:
    - Selecciona la opción "6. Guardar tareas" en el menú.
    - Ingresa el nombre del archivo JSON donde deseas guardar las tareas actuales.

## Estado del proyecto
El proyecto está en una fase inicial de desarrollo. Las funcionalidades básicas están implementadas y se están realizando pruebas unitarias para asegurar su correcto funcionamiento. Se planean futuras mejoras, como la integración con servicios en la nube para sincronizar tareas entre dispositivos.
