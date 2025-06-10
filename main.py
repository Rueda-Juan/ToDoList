import sqlite3
from .CRUD_Usuario import (
    crear_usuario,
    obtener_usuario,
    obtener_usuario_por_correo
)
from .CRUD_Tarea import (
    crear_tarea,
    obtener_tarea,
    obtener_tareas_por_usuario,
    actualizar_tarea,
    eliminar_tarea
)
from .Servicios import (
    login,
    verificar_credenciales,
    registrar
)
from sqlite3 import IntegrityError
from sqlite3 import Error

#comando para ejecutar main
#   python -m proyectoFinalBD.main

def conectar_db():
    return sqlite3.connect("DbUsuario.db")

# ----------- MENÚ DE TAREAS -----------
def menu_tareas(conn, id_usuario):
    while True:
        print("\n=== Menú de Tareas ===")
        print("1. Ver tareas")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Marcar tarea como completada")
        print("6. Cerrar sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tareas = obtener_tareas_por_usuario(conn, id_usuario)
            if tareas:
                print("\n Tus tareas:")
                for t in tareas:
                    estado = "Completado" if t[5] else "Pendiente"
                    print(f"[{t[0]}] {t[2]} - {estado}")
                    if t[3]:
                        print(f"   {t[3]}")
            else:
                print("No tienes tareas.")
        elif opcion == "2":
            titulo = input("Título de la tarea: ").strip()
            descripcion = input("Descripción (opcional): ").strip()
            crear_tarea(conn, id_usuario, titulo, descripcion)
            print("Tarea creada.")

        elif opcion == "3":
            id_tarea = input("ID de la tarea a editar: ").strip()
            titulo = input("Nuevo título (enter para dejar igual): ").strip()
            descripcion = input("Nueva descripción (enter para dejar igual): ").strip()
            if not id_tarea.isdigit():
                print("ID inválido.")
            else:
                actualizado = actualizar_tarea(conn, int(id_tarea), titulo if titulo else None, descripcion if descripcion else None)
                print("Tarea actualizada." if actualizado else " No se pudo actualizar.")

        elif opcion == "4":
            id_tarea = input("ID de la tarea a eliminar: ").strip()
            if not id_tarea.isdigit():
                print("ID inválido.")
            else:
                confirmado = input("¿Estás seguro? (s/n): ").strip().lower()
                if confirmado == "s":
                    eliminado = eliminar_tarea(conn, int(id_tarea))
                    print("Tarea eliminada." if eliminado else "No se encontró la tarea.")

        elif opcion == "5":
            id_tarea = input("ID de la tarea a marcar como completada: ").strip()
            if not id_tarea.isdigit():
                print("ID inválido.")
            else:
                completada = actualizar_tarea(conn, int(id_tarea), completada=1)
                print(" Tarea marcada como completada." if completada else " No se pudo completar la tarea.")

        elif opcion == "6":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# ----------- MENÚ PRINCIPAL -----------
def main():
    conn = conectar_db()
    try:
        while True:
            print("\n=== Bienvenido a la App de Tareas ===")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                id_usuario = login(conn)
                if id_usuario:
                    menu_tareas(conn, id_usuario)
            elif opcion == "2":
                registrar(conn)
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
