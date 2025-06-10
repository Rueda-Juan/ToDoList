-- Conuslta para creae una tarea
INSERT INTO Tarea(id_usuario, titulo, descripcion) VALUES (?,?,?);

-- Consulta para obtener una tarea
SELECT * FROM Tarea WHERE id_tarea = ?;

-- Consulta para obtener todas las tareas
SELECT * FROM Tarea WHERE id_usuario = ?;

-- Consulta para eliminar tarea
DELETE FROM Tarea WHERE id_tarea = ?;

