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