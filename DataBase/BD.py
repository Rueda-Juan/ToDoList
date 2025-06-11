import sqlite3

def crear_tablas(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tarea(
            id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
            completada INTEGER DEFAULT 0,
            FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
        )
    ''')

    conn.commit()
