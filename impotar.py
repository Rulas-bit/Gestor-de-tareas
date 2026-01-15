# importar tareas

def importar_tareas(nombre_archivo):
    import json
    try:
        with open(nombre_archivo, "r") as archivo:  # abre el archivo en modo lectura.
            tareas = json.load(archivo)  # carga la lista de tareas desde el archivo JSON.
        print(f"Tareas importadas desde {nombre_archivo}")
        return tareas
    except FileNotFoundError: # si el archivo no existe
        print(f"No se encontró el archivo {nombre_archivo}.")
        return [] # devuelve una lista vacía si el archivo no existe
# fin importar tareas.