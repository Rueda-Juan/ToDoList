import sqlite3
from sqlite3 import Error
#TAREA
# CREATE
def crear_tarea(conn, id_usuario, titulo, descripcion=None):
    sql = '''INSERT INTO Tarea(id_usuario, titulo, descripcion) VALUES (?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_usuario, titulo, descripcion))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al crear tarea: {e}")
        return None

# READ
def obtener_tarea(conn, id_tarea):
    sql = "SELECT * FROM Tarea WHERE id_tarea = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_tarea,))
        return cursor.fetchone()
    except Error as e:
        print(f"Error al obtener tarea: {e}")
        return None

# READ ALL
def obtener_tareas_por_usuario(conn, id_usuario):
    sql = "SELECT * FROM Tarea WHERE id_usuario = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_usuario,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error al obtener tareas del usuario: {e}")
        return []

# UPDATE
def actualizar_tarea(conn, id_tarea, titulo=None, descripcion=None, completada=None):
    updates = []
    params = []

    if titulo is not None:
        updates.append("titulo = ?")
        params.append(titulo)
    if descripcion is not None:
        updates.append("descripcion = ?")
        params.append(descripcion)
    if completada is not None:
        updates.append("completada = ?")
        params.append(completada)

    if not updates:
        return False

    params.append(id_tarea)
    sql = f"UPDATE Tarea SET {', '.join(updates)} WHERE id_tarea = ?"

    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error al actualizar tarea: {e}")
        return False

# DELETE
def eliminar_tarea(conn, id_tarea):
    sql = "DELETE FROM Tarea WHERE id_tarea = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id_tarea,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error al eliminar tarea: {e}")
        return False