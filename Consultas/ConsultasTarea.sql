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