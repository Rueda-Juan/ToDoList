import pytest
import sqlite3
from unittest.mock import patch
from Utils import Servicios
from CRUD.CRUD_Usuario import crear_usuario, obtener_usuario_por_correo
import bcrypt

# Setup: base de datos en memoria
@pytest.fixture
def conexion():
    conn = sqlite3.connect(":memory:")
    conn.execute('''CREATE TABLE Usuario (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        correo TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )''')
    yield conn
    conn.close()

def test_verificar_credenciales_valido(conexion):
    correo = "test@mail.com"
    nombre = "Test"
    password = "1234"
    hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    crear_usuario(conexion, correo, nombre, hash)

    usuario = Servicios.verificar_credenciales(conexion, correo, password)
    assert usuario is not None
    assert usuario[1] == correo

@patch("builtins.input", side_effect=["nuevo@mail.com", "Nuevo Nombre", "abcd1234"])
def test_registrar_usuario(mock_inputs, conexion):
    Servicios.registrar(conexion)
    usuario = obtener_usuario_por_correo(conexion, "nuevo@mail.com")
    assert usuario is not None

@patch("builtins.input", side_effect=["login@mail.com", "1234"])
def test_login_valido(mock_inputs, conexion):
    # Crear usuario primero
    hash = bcrypt.hashpw("1234".encode(), bcrypt.gensalt()).decode()
    crear_usuario(conexion, "login@mail.com", "LoginUser", hash)

    with patch("Utils.Servicios.tareas_pendientes"):
        id_usuario = Servicios.login(conexion)
        assert id_usuario is not None