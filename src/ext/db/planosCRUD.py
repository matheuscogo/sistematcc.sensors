from ..site.model.Plano import Plano
from ..site.model.Dia import Dia
from ..db import session
from werkzeug.wrappers import Response, Request
import json


def consultarPlano(id):  # Read
    try:
        plano = session.query(Plano.Plano).filter_by(id=id).first()
        return plano
    except Exception as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarQuantidade(id): # Read
    try:
        quantidades = session.query(Dia.quantidade).filter_by(plano=id).all()
        array = list()
        for quantidade in quantidades:
            array.append(quantidade[0])
        json_str = json.dumps(array)
        return json_str
    except:
        return False
