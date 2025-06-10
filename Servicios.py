import sqlite3
from sqlite3 import IntegrityError
from sqlite3 import Error
from proyectoFinalBD.CRUD_Usuario import (
    crear_usuario,
    obtener_usuario,
    obtener_usuario_por_correo
)
from proyectoFinalBD.CRUD_Tarea import (
    crear_tarea,
    obtener_tarea,
    obtener_tareas_por_usuario,
    actualizar_tarea,
    eliminar_tarea
)
from .Validaciones import (
    es_correo_valido,
    es_nombre_valido
)
import bcrypt

def login(conn):
    print("\n=== Inicio de sesión ===")
    correo = input("Correo: ").strip()
    contraseña = input("Contraseña: ").strip()

    usuario = verificar_credenciales(conn, correo, contraseña)
    if usuario:
        print(f"\n¡Bienvenido {usuario[2]}!\n")  # usuario[2] = nombre
        tareas_pendientes(conn, usuario[0])
        return usuario[0]  # usuario[0] = id_usuario
    else:
        print("\n Credenciales incorrectas.\n")
        return None

def verificar_credenciales(conn, correo, contraseña):
    usuario = obtener_usuario_por_correo(conn, correo.strip().lower())
    if usuario is not None:
        hash_guardado = usuario[3]
        # vuelve la contraseña(string normal), 
        # y la contraseña guardada (de string normal, paso a bytes y luego a string hasheado)
        # de string la pasa a bytes y las compara
        if bcrypt.checkpw(contraseña.encode(), hash_guardado.encode()):
            return usuario
    return None


def registrar(conn):
    print("\n=== Registro de nuevo usuario ===")
    #====VALIDACIONES=====
    correo = input("Correo: ").strip().lower()
    if not es_correo_valido(correo):
        print("Formato de correo inválido.")
        return

    nombre = input("Nombre: ").strip()
    if not es_nombre_valido(nombre):
        print("El nombre solo puede contener letras y espacios.")
        return
    contraseña = input("Contraseña: ").strip()

    #====HASHING====
    #guarda la contraseña de forma mas segura
    hash_bytes = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())
    hash_str = hash_bytes.decode()
    
    try:
        id_usuario = crear_usuario(conn, correo, nombre, hash_str)
        if id_usuario:
            print(" Usuario registrado exitosamente. Puedes iniciar sesión ahora.")
        else:
            print(" No se pudo registrar el usuario.")
    except IntegrityError as e:
        if "UNIQUE constraint failed: Usuario.correo" in str(e):
            print(" El correo ya está registrado. Intenta con otro.")
        else:
            print(f" Error al registrar el usuario: {e}")

def tareas_pendientes(conn,id_usuario):
    tareas = obtener_tareas_por_usuario(conn, id_usuario)
    pendientes = [t for t in tareas if t[5] == 0]  # t[5] = completada

    if not tareas:
        print("No tenés tareas creadas.")
    elif pendientes:
        print(f"Tenés {len(pendientes)} tarea(s) sin completar.")
    else:
        print("¡Todas tus tareas están completadas! No hay nada pendiente.")