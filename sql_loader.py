
# Cargara las consultas de SQL por nombre

import os

def cargar_sql_por_nombre(nombre_archivo, nombre_consulta):
    # Obtiene la ruta absoluta al archivo actual (sql_loader.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Se mueve a la carpeta padre del archivo actual (proyectoFinalBD)
    proyecto_dir = os.path.join(base_dir)
    
    # Une el path al archivo SQL (por ejemplo, Consultas/ConsultasUsuario.sql)
    ruta_sql = os.path.join(proyecto_dir, nombre_archivo)

    if not os.path.isfile(ruta_sql):
        raise FileNotFoundError(f"No se encontró el archivo SQL: {ruta_sql}")

    with open(ruta_sql, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    secciones = contenido.split('-- ')
    for seccion in secciones:
        if seccion.startswith(nombre_consulta):
            return seccion[len(nombre_consulta):].strip()

    # si algo falla, mostrara la consulta que no se encontro
    raise ValueError(f"Consulta '{nombre_consulta}' no encontrada en {ruta_sql}")