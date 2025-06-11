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

## Consultas SQL
### consultas SQL para Usuario
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

### Constula SQL para Tarea
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