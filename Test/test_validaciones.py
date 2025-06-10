from Utils.Validaciones import es_correo_valido, es_nombre_valido

# ----------- Tests para es_correo_valido -----------

def test_correo_valido_basico():
    assert es_correo_valido("test@mail.com")

def test_correo_valido_con_punto():
    assert es_correo_valido("usuario.nombre@mail.co")

def test_correo_invalido_sin_arroba():
    assert not es_correo_valido("usuarionombremail.com")

def test_correo_invalido_sin_dominio():
    assert not es_correo_valido("usuario@.com")

def test_correo_invalido_sin_extension():
    assert not es_correo_valido("usuario@correo")

# ----------- Tests para es_nombre_valido -----------

def test_nombre_valido_sin_espacios():
    assert es_nombre_valido("Juan")

def test_nombre_valido_con_espacios():
    assert es_nombre_valido("María Pérez")

def test_nombre_valido_con_acentos_y_ñ():
    assert es_nombre_valido("José Ñandú")

def test_nombre_invalido_con_numeros():
    assert not es_nombre_valido("Juan123")

def test_nombre_invalido_con_simbolos():
    assert not es_nombre_valido("Ana!@#")
