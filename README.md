Proyecto #2
Integrantes:Matías Acuña Barquero, Dylan Witcher Ramírez, Isaac Brenes Hidalgo y Naomi González Madriz

Idea: Realizar un gestor de tareas, el cual puede tener pendientes, puede agregar tareas, marcar tareas como hechas y lleva un registro guardable para mantener el orden.

Boceto:
import os

def ctareas():
    if os.path.exists("tareas.txt"):
        with open("tareas.txt", "r") as archivo:
            return archivo.readlines()
    else:
        return []

def gtareas(tareas):
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def mtareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea.strip()}")

def agtarea(tareas):
    nuevat = input("Ingrese la nueva tarea: ")
    tareas.append(nuevat)
    gtareas(tareas)
    print("Tarea agregada")

def comtarea(tareas):
    mostareas(tareas)
    num_tarea = int(input("Ingrese el número de la tarea completada: "))
    if 1 <= num_tarea <= len(tareas):
        del tareas[num_tarea - 1]
        gtareas(tareas)
        print("Tarea completada")
    else:
        print("Número de tarea inválido")

def eliminar_tarea(tareas):
    mostareas(tareas)
    num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
    if 1 <= num_tarea <= len(tareas):
        del tareas[num_tarea - 1]
        gtareas(tareas)
        print("Tarea eliminada")
    else:
        print("Número de tarea inválido")

def mostrar_menu():
    print("\n GESTOR DE TAREAS")
    print("1. Ver tareas pendientes")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tareas = cargar_tareas()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostareas(tareas)
        elif opcion == "2":
            agtarea(tareas)
        elif opcion == "3":
            comtarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Bálvalo")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
