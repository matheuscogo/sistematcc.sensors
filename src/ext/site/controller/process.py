from ext.db import registroCRUD


def save(registro):
    registro = registroCRUD.cadastrarRegistro(registro)
