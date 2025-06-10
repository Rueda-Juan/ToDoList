import sqlite3

# Crea una base de datos llamada "DbUsuario.db"
# Si la base de datos ya existe, se conceta a la misma
conexion = sqlite3.connect("DbUsuario.db")


# Creamos el cursor
cursor = conexion.cursor()

# Creacion de la tabla usuario
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario(
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        contraseña TEXT NOT NULL
    )
''')

#Creacion de la tabla Tarea
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tarea(
        id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
        fecha_limite TEXT,
        completada INTEGER DEFAULT 0,
        FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE)
''')

conexion.commit()
conexion.close()