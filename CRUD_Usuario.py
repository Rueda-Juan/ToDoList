import sqlite3
from sqlite3 import Error

#USUARIO
#CREATE
def crear_usuario(conn, correo, nombre, contraseña):
  sql = '''INSERT INTO Usuario(correo, nombre, contraseña)
            VALUES(?,?,?)'''
  try:
      cursor = conn.cursor()
      cursor.execute(sql, (correo, nombre, contraseña))
      conn.commit()
      return cursor.lastrowid
  except Error as e:
      print(f"Error al crear usuario: {e}")
  return None

#READ
def obtener_usuario(conn, id_usuario):
  sql = "SELECT * FROM Usuario WHERE id_usuario = ?"
  try:
      cursor = conn.cursor()
      cursor.execute(sql, (id_usuario,))
      return cursor.fetchone()
  except Error as e:
      print(f"Error al obtener usuario por id: {e}")
  return None

def obtener_usuario_por_correo(conn, correo):
  sql = "SELECT * FROM Usuario WHERE correo = ?"
  try:
      cursor = conn.cursor()
      cursor.execute(sql, (correo,))
      return cursor.fetchone()
  except Error as e:
      print(f"Error al obtener usuario por correo: {e}")
  return None

#UPDATE
def actualizar_usuario(conn, id_usuario, nombre=None, contraseña=None):
  updates = []
  params = []
  
  if nombre:
      updates.append("nombre = ?")
      params.append(nombre)
  if contraseña:
      updates.append("contraseña = ?")
      params.append(contraseña)
      
  if not updates:
      return False
      
  params.append(id_usuario)
  sql = f"UPDATE Usuario SET {','.join(updates)} WHERE id_usuario = ?"
  
  try:
      cursor = conn.cursor()
      cursor.execute(sql, params)
      conn.commit()
      return cursor.rowcount > 0
  except Error as e:
      print(f"Error al actualizar usuario: {e}")
  return False
  
#DELETE
def eliminar_usuario(conn, id_usuario):
  sql = "DELETE FROM Usuario WHERE id_usuario = ?"
  try:
      cursor = conn.cursor()
      cursor.execute(sql, (id_usuario,))
      conn.commit()
      return cursor.rowcount > 0
  except Error as e:
      print(f"Error al eliminar usuario: {e}")
  return False
