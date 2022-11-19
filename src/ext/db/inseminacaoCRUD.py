from ast import arg
from datetime import datetime
from re import I
from xmlrpc.client import ResponseError
from ..site.model.Inseminacao import Inseminacao
from ..site.model.Matriz import Matriz
from ..site.model.Confinamento import Confinamento
from ..site.model.Plano import Plano
# from ..site.model.Inseminacao import InseminacaoSchema
from ..db import db
from werkzeug.wrappers import Response, Request
import json


def consultarInseminacaoPelaMatriz(matrizId):  # Read
    try:
        inseminacao = db.session.query(Inseminacao).filter_by(matrizId=matrizId, active=True, deleted=False).first()
        return inseminacao
    except Exception as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
