import os
import datetime

# Función para agregar una tarea
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD, dejar en blanco si no tiene): ")
    if fecha_vencimiento:
        try:
            fecha_vencimiento = datetime.datetime.strptime(fecha_vencimiento, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de fecha inválido. La tarea se guardará sin fecha de vencimiento.")
            fecha_vencimiento = None
    else:
        fecha_vencimiento = None
    
    tarea = f"Título: {titulo}\nDescripción: {descripcion}\nFecha de Vencimiento: {fecha_vencimiento}\n"
    
    with open("tareas_pendientes.txt", "a") as file:
        file.write(tarea)
    
    print("Tarea agregada con éxito!")

# Función para listar tareas pendientes
def listar_tareas():
    try:
        with open("tareas_pendientes.txt", "r") as file:
            tareas = file.readlines()
        
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("\nTAREAS PENDIENTES:\n")
            for i, tarea in enumerate(tareas, start=1):
                print(f"Tarea {i}:\n{tarea}")
    except FileNotFoundError:
        print("No hay tareas pendientes.")

# Función para marcar una tarea como completada
def marcar_completada():
    listar_tareas()
    tarea_a_completar = input("\nIngrese el número de la tarea que desea marcar como completada (0 para cancelar): ")
    
    if tarea_a_completar.isdigit():
        tarea_a_completar = int(tarea_a_completar)
        if tarea_a_completar > 0:
            try:
                with open("tareas_pendientes.txt", "r") as file:
                    tareas = file.readlines()
                
                if tarea_a_completar <= len(tareas):
                    tarea_completada = tareas.pop(tarea_a_completar - 1)
                    
                    with open("tareas_pendientes.txt", "w") as file:
                        file.writelines(tareas)
                    
                    with open("tareas_completadas.txt", "a") as file:
                        file.write(tarea_completada)
                    
                    print("Tarea marcada como completada.")
                else:
                    print("Número de tarea no válido.")
            except FileNotFoundError:
                print("No hay tareas pendientes.")
        elif tarea_a_completar == 0:
            print("Operación cancelada.")
        else:
            print("Número de tarea no válido.")
    else:
        print("Número de tarea no válido.")

# Función para mostrar tareas vencidas o próximas a vencerse
def mostrar_tareas_vencidas():
    try:
        with open("tareas_pendientes.txt", "r") as file:
            tareas = file.readlines()
        
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("\nTAREAS VENCIDAS O PRÓXIMAS A VENCERSE:\n")
            today = datetime.date.today()
            for tarea in tareas:
                lines = tarea.split("\n")
                for line in lines:
                    if line.startswith("Fecha de Vencimiento: "):
                        fecha_str = line.replace("Fecha de Vencimiento: ", "")
                        fecha_vencimiento = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
                        if fecha_vencimiento < today:
                            print(f"Tarea:\n{tarea}")
                            print("Esta tarea está vencida.\n")
                        elif fecha_vencimiento == today:
                            print(f"Tarea:\n{tarea}")
                            print("Esta tarea vence hoy.\n")
            print("Fin de la lista.")
    except FileNotFoundError:
        print("No hay tareas pendientes.")

# Función principal
def main():
    while True:
        print("\n===== GESTIÓN DE TAREAS =====")
        print("1. Agregar una tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas vencidas o próximas a vencerse")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            mostrar_tareas_vencidas()
        elif opcion == "5":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
