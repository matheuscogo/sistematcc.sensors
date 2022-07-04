from genericpath import exists
from queue import Empty

from responses import activate, delete

from ext.site.model import Inseminacao
from ..site.model import Aviso
from ..site.model import Registro
from ..site.model.Confinamento import Confinamento
from ..db import db
import datetime
from werkzeug.wrappers import Response, Request
from xmlrpc.client import ResponseError
import json
from ..site.model import Dia
from ..site.model.Plano import Plano
from ..site.model.Matriz import Matriz
from ..site.model.Registro import Registro
from ..db import db
from sqlalchemy.sql import func
from datetime import datetime, timedelta


def cadastrarAviso(args):  # Create
    try:
        dataAviso = int(args['dataAviso'])
        confinamentoId = int(args['confinamentoId'])

        dataAviso = datetime.strftime(
            datetime.fromtimestamp(dataAviso/1000.0), '%d/%m/%y')
        if not confinamentoId:
            raise Exception(ResponseError)

        if not dataAviso:
            raise Exception(ResponseError)

        db.session.add(Aviso.Aviso(
            confinamentoId=confinamentoId,
            dataAviso=dataAviso)
        )

        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Aviso cadastrado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarConfinamento(id):  # Read
    try:
        confinamento = db.session.query(
            Confinamento).filter_by(id=id, active=True).first()
        return confinamento
    except BaseException as e:
        return str(e)


def consultarConfinamentos():  # Read
    try:
        response = db.session.query(
            Confinamento.Confinamento).filter_by(active=True).all()

        confinamentos = []

        for confinamento in response:
            matrizDescription = db.session.query(Matriz).filter_by(
                id=int(confinamento.matrizId), deleted=False).first()
            planoDescription = db.session.query(Plano).filter_by(
                id=int(confinamento.planoId), active=True, deleted=False).first()
            obj = {"id": confinamento.id, "planoDescription": planoDescription.nome,
                   "matrizDescription": matrizDescription.rfid, "dataConfinamento": confinamento.dataConfinamento}
            confinamentos.append(obj)

        return confinamentos
    except BaseException as e:
        return str(e)


def atualizarConfinamento(args):
    try:
        id = args['id']
        dataConfinamento = args['dataConfinamento']
        plano = args['plano']
        matriz = args['matriz']
        confinamento = db.session.query(Confinamento).filter_by(id=id).first()
        confinamento.dataConfinamento = dataConfinamento
        confinamento.matriz = matriz
        confinamento.plano = plano
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Confinamento atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirConfinamento(id):  # Delete
    try:
        confinameto = db.session.query(Confinamento).filter_by(id=id).first()
        db.session.delete(confinameto)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Confinameto excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def getConfinamentoByMatriz(matrizId):
    try:
        confinamento = db.session.query(Confinamento.Confinamento).filter_by(
            matrizId=matrizId, active=True).first()
        return confinamento
    except BaseException as e:
        return str(e)


def getQuantityForMatriz(matrizId):
    try:
        confinamento = db.session.query(Confinamento.Confinamento).filter_by(
            matrizId=matrizId, active=True).first()
        matrizId = confinamento.matrizId
        planoId = confinamento.planoId
        dataEntrada = datetime.today().strftime('%d/%m/%y')

        day = getDaysInConfinament(matrizId=matrizId)
        dayQuantity = db.session.query(Dia.Dias.quantidade).filter_by(
            planoId=planoId, dia=day).first()[0]
        totalQuantity = db.session.query(func.sum(Registro.quantidade)).filter_by(
            matrizId=matrizId, dataEntrada=dataEntrada).first()[0]

        if totalQuantity is None:
            totalQuantity = 0

        total = dayQuantity - totalQuantity

        if total <= 0:
            total = 0

        return total
    except BaseException as e:
        return e.args[0]


def canOpenDoor(matrizId):
    try:

        hasInseminacao = db.session.query(Inseminacao.Inseminacao.query.filter_by(
            matrizId=matrizId, active=True).exists()).scalar()

        if not hasInseminacao:
            return "Matriz não possui inseminação valida"

        day = getDaysInConfinament(matrizId=matrizId)

        # paramters = getParameters
        if day >= 110:
            # Aviso já foi inserido?
            # if avisoInserido:
            return True
        else:
            return False
    except BaseException as e:
        return e.args[0]


def verifyDaysToOpen():
    try:
        inseminacao = db.session.query(
            Inseminacao.Inseminacao).filter_by(active=True).all()

        for item in inseminacao:
            day = getDaysInConfinament(matrizId=item.matrizId)

            # paramters = getParameters
            if day >= 2:
                # Aviso já foi inserido?
                # if avisoInserido:
                return True
            else:
                return False
    except BaseException as e:
        return e.args[0]


def getDaysInConfinament(matrizId):
    confinamento = db.session.query(Confinamento.Confinamento).filter_by(
        matrizId=matrizId, active=True).first()
    dataEntrada = datetime.strptime(confinamento.dataConfinamento, '%d/%m/%y')
    dataAtual = datetime.today()
    days = dataAtual - dataEntrada
    print("DIA ENTRADA = " + str(dataEntrada))
    print("DIA ATUAL = " + str(dataAtual))
    return days.days
