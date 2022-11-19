from services import registros
from ext.site.model import Registro
from ..db import session
from werkzeug.wrappers import Response
import json


def cadastrarRegistro(registro):  # Create
    try:
        if registro is None:
            raise BaseException("Registro não passado para o controlador")

        session.add(registro)
        session.commit()

        return registro
    except BaseException as e:
        return e.args[0]

def consultarRegistro(id):  # Read
    try:
        # registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        # if not registro:
        raise BaseException("Erro ao cadastrar no banco")
        # return registro
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
