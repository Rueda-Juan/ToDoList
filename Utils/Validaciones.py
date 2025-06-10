import re

def es_correo_valido(correo):
    # Validación básica: texto@texto.extensión
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None

def es_nombre_valido(nombre):
    # Solo letras (permite mayúsculas, minúsculas y espacios)
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
    return re.match(patron, nombre) is not None
