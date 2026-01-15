
# listar tareas.

def listar_tareas (tareas):
    if not tareas :
        print("no hay tareas") 
        return
    print("\nlista de tareas:")
    for tarea in tareas:
        print(f"{tarea["id"]} - {tarea["titulo"]} - ({tarea["estado"]})") # muestra id, titulo y estado de cada tarea.
# fin listar tareas.
   