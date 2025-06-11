# ToDoList

## Integrantes
- Rueda Juan Bautista
- Rodriguez Javier Agustin
  

## Modelo Conceptual de la Base De Datos
<p align="center">
  <img src="img/modelo coneptual de BS usuario-tarea.png" alt="Captura de pantalla" width="300"/>
</p>

## Diagrama Entidad Relacion de la base de datos
<p align="center">
  <img src="img/Diagrama entidad relacion BD usuario-tarea.png" alt="Captura de pantalla" width="500"/>
</p>

## Motor Elegido
SQLite
- Se eligio SQLites debido a que ambos integrantes ya teniamos un poco de experiencia trabajando con este motor

## Consultas SQL

### Creacion de la tabla Usuario
```sql
    CREATE TABLE IF NOT EXISTS Usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
```
#### consultas SQL para Usuario
```sql
-- crear_usuario
INSERT INTO Usuario(correo, nombre, contraseña) VALUES (?, ?, ?);

-- obtener_usuario
SELECT * FROM Usuario WHERE id_usuario = ?;

-- obtener_usuario_por_correo
SELECT * FROM Usuario WHERE correo = ?;

-- actualizar_usuario
UPDATE Usuario SET {campos} WHERE id_usuario = ?;

-- eliminar_usuario
DELETE FROM Usuario WHERE id_usuario = ?;
```
### Creacion de la tabla Tarea
``` sql
    CREATE TABLE IF NOT EXISTS Tarea(
            id_tarea INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
            completada INTEGER DEFAULT 0,
            FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
        )
```
#### Constula SQL para Tarea
```sql
-- crear_tarea
INSERT INTO Tarea(id_usuario, titulo, descripcion) VALUES (?, ?, ?);

-- obtener_tarea
SELECT * FROM Tarea WHERE id_tarea = ?;

-- obtener_tareas_por_usuario
SELECT * FROM Tarea WHERE id_usuario = ?;

-- actualizar_tarea
UPDATE Tarea SET {campos} WHERE id_tarea = ?;

-- eliminar_tarea
DELETE FROM Tarea WHERE id_tarea = ?;
```
## Estructura del Proyecto
```text
TodoList/
├── CRUD/                  
│   |__CRUD_Usuario.py            
│   └──CRUD_Tarea.py   
├── DataBase/                     
│   |── Consultas/
│   |   └── ConsultasTarea.sql             
│   |   └── ConsultasUsuario.sql    
│   |── DB.py   
├── Test/                     
│   ├── test_tarea.py             
│   └── test_usuario            
└── Utils/                    
|   └── Servicios.py
|   └── sql_loader.py
|   └── Validaciones.py
├── main.py 
```

##### Clonar Repositorio
```git
  git clone https://github.com/Rueda-Juan/ToDoList.git
```

##### Acceder a la carpeta ToDoList
```git
  git cd ToDoList
```

##### Ejecutar el proyecto
```
  python -m main
```

##### Ejecutar los Test
```
  python -m pytest
```
##### Instalar dependencias de los Test
```
  pip install pytest
```

##### Instalar dependencias de bcrypt para encriptar contraseñas
```
  pip install bcrypt
```