from ext.db import registroCRUD
from ext.db import alimentadorCRUD


def query(hash):
    alimentador = alimentadorCRUD.consultarAlimentadores(hash)
    return alimentador


def save(registro):
    alimentador = registroCRUD.cadastrarRegistro(registro)
    return alimentador
