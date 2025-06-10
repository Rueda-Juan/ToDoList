import sqlite3
from sqlite3 import Error
from proyectoFinalBD.CRUD_Usuario import crear_usuario, obtener_usuario, actualizar_usuario, eliminar_usuario



# Crear tabla temporal para pruebas unitarias automatizadas
def crear_tabla_usuario(conexion):
    sql = '''
    CREATE TABLE Usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        correo TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
    '''
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
    except Error as e:
        print(f"Error al crear la tabla: {e}")



# ----------------------
# TESTS usando pytest
# ----------------------

import pytest

@pytest.fixture

# Conexion auxiliar temporal a la base de datos
def conexion():
    conexionAuxiliar = sqlite3.connect(":memory:")
    crear_tabla_usuario(conexionAuxiliar)
    yield conexionAuxiliar
    conexionAuxiliar.close()

# -----------------------
# 4 METODOS A TESTAR
# crear_usuario
# obtener_usuario
# actualizar_usuario
# eliminar_usuario
# ----------------------

def test_crear_usuario(conexion):
    id_usuario = crear_usuario(conexion, "test@mail.com", "Test", "1234")
    assert id_usuario is not None, "❌ El ID de usuario no debería ser None"



def test_obtener_usuario(conexion):
    id_usuario = crear_usuario(conexion, "user@mail.com", "User", "pass")
    usuario = obtener_usuario(conexion, id_usuario)
    assert usuario[1] == "user@mail.com", f"❌ Se esperaba 'user@mail.com', pero se obtuvo '{usuario[1]}'"
    assert usuario[2] == "User", f"❌ Se esperaba nombre 'User', pero se obtuvo '{usuario[2]}'"


def test_actualizar_usuario(conexion):
    id_usuario = crear_usuario(conexion, "a@mail.com", "A", "1")
    actualizado = actualizar_usuario(conexion, id_usuario, nombre="Nuevo")
    assert actualizado, "❌ No se actualizó el usuario correctamente"

    usuario = obtener_usuario(conexion, id_usuario)
    assert usuario[2] == "Nuevo", f"❌ Nombre incorrecto: esperado 'Nuevo', obtenido '{usuario[2]}'"



def test_eliminar_usuario(conexion):
    id_usuario = crear_usuario(conexion, "b@mail.com", "B", "2")
    eliminado = eliminar_usuario(conexion, id_usuario)
    assert eliminado, "❌ El usuario no se eliminó correctamente"

    usuario = obtener_usuario(conexion, id_usuario)
    assert usuario is None, "❌ El usuario eliminado aún existe en la base de datos"