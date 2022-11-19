from sqlalchemy.sql.elements import Null
from ..site.model.Dia import Dia
from ..site.model.Confinamento import Confinamento
from ..db import session
from werkzeug.wrappers import Response, Request
import json


def consultarQuantidade(planoId, dia):  # Read
    try:
        quantidade = session.query(Dia.quantidade).filter_by(dia=dia, planoId=planoId).first()
        return quantidade
    except Exception as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
