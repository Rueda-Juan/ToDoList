import sqlite3
import pytest
import os
import sys


# Añadir la ruta del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from proyectoFinalBD.CRUD_Tarea import (
    crear_tarea,
    obtener_tarea,
    obtener_tareas_por_usuario,
    actualizar_tarea,
    eliminar_tarea
)

from proyectoFinalBD.CRUD_Usuario import crear_usuario  # Para insertar un usuario y asignarle tareas

# ----------------------
# Setup de Base de Datos
# ----------------------

def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE Usuario (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            correo TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            contraseña TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE Tarea (
            id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            completada BOOLEAN DEFAULT 0,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
        );
    ''')
    conexion.commit()

@pytest.fixture
def conexion():
    conexionAuxiliar = sqlite3.connect(":memory:")
    crear_tablas(conexionAuxiliar)
    yield conexionAuxiliar
    conexionAuxiliar.close()

# ----------------------
# TESTS
# ----------------------

def test_crear_tarea(conexion):
    id_usuario = crear_usuario(conexion, "mail@ejemplo.com", "Nombre", "clave")
    id_tarea = crear_tarea(conexion, id_usuario, "Comprar pan", "Ir a la panadería")
    assert id_tarea is not None, "❌ No se creó la tarea"

def test_obtener_tarea(conexion):
    id_usuario = crear_usuario(conexion, "a@mail.com", "Ana", "123")
    id_tarea = crear_tarea(conexion, id_usuario, "Estudiar", "Repasar para el examen")
    tarea = obtener_tarea(conexion, id_tarea)
    assert tarea is not None
    assert tarea[2] == "Estudiar", f"❌ Se esperaba 'Estudiar', se obtuvo '{tarea[2]}'"

def test_obtener_tareas_por_usuario(conexion):
    id_usuario = crear_usuario(conexion, "b@mail.com", "Beto", "pass")
    crear_tarea(conexion, id_usuario, "Lavar ropa")
    crear_tarea(conexion, id_usuario, "Planchar")
    tareas = obtener_tareas_por_usuario(conexion, id_usuario)
    assert len(tareas) == 2, f"❌ Se esperaban 2 tareas, se obtuvieron {len(tareas)}"

def test_actualizar_tarea(conexion):
    id_usuario = crear_usuario(conexion, "c@mail.com", "Carlos", "clave")
    id_tarea = crear_tarea(conexion, id_usuario, "Leer", "Libro de historia")
    actualizado = actualizar_tarea(conexion, id_tarea, titulo="Leer novela", completada=True)
    assert actualizado, "❌ No se actualizó la tarea correctamente"
    tarea = obtener_tarea(conexion, id_tarea)
    assert tarea[2] == "Leer novela"
    assert tarea[4] == 1  # completada == True

def test_eliminar_tarea(conexion):
    id_usuario = crear_usuario(conexion, "d@mail.com", "Dario", "clave")
    id_tarea = crear_tarea(conexion, id_usuario, "Sacar la basura")
    eliminado = eliminar_tarea(conexion, id_tarea)
    assert eliminado, "❌ No se eliminó la tarea correctamente"
    tarea = obtener_tarea(conexion, id_tarea)
    assert tarea is None, "❌ La tarea aún existe luego de ser eliminada"