from datetime import datetime
from ext.site.model import Matriz
from ext.site.model import Confinamento
from ext.site.model import Alimentador
from ext.site.model import Dia
from ext.db import session, func
from werkzeug.wrappers import Response
import json
import uuid


def cadastrarAlimentador(alimentador):  # Create
    try:
        session.add(alimentador)
        session.commit()
        return Response(response=json.dumps("{success: true, message: Alimentador cadastrada com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarAlimentadores(hash):  # Read
    try:
        alimentador = session.query(func.sum(
            Alimentador.quantidade).label("quantidadeTotal"), Alimentador.hash, Alimentador.matrizId).filter_by(hash=hash).group_by(Alimentador.hash).first()
        return alimentador
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarMatriz(id):  # Read
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(id=id).first()
        if not matriz:
            raise Exception(matriz)
        return matriz
    except Exception as e:
        return e.args[0]


def getMatrizByRfid(rfid):  # Read
    try:
        matriz = db.session.query(Matriz).filter_by(rfid=rfid).first()
        if not matriz:
            raise Exception(matriz)
        return matriz
    except Exception as e:
        return e.args[0]


def atualizarMatriz(args):  # Update
    try:
        id = int(args['id'])
        rfid = str(args['rfid'])
        numero = int(args['numero'])
        ciclos = int(args['ciclos'])
        matriz = db.session.query(Matriz.Matriz).filter_by(id=id).first()
        matriz.rfid = rfid
        matriz.numero = numero
        matriz.ciclos = ciclos
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Matriz atualizada com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirMatriz(id):  # Delete
    try:
        matriz = db.session.query(Matriz.Matriz).filter_by(id=id).first()
        db.session.delete(matriz)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Matriz excluida com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarMatrizRFID(rfid):  # Read
    try:
        matriz = session.query(Matriz).filter_by(rfid=rfid).first()

        confinamento = session.query(Confinamento).filter_by(
            matrizId=matriz.id).first()

        day = (confinamento.dataConfinamento - datetime.now()).day

        dia = session.query(Dia).filter_by(
            id=confinamento.planoId, dia=day).first()

        matriz.hash = uuid.uuid4()
        matriz.entrada = datetime.now()
        confinamento

        return matriz
    except Exception as e:
        return e.args[0]


def existsRFID(rfid):
    exists = db.session.query(db.exists().where(
        Matriz.Matriz.rfid == rfid)).scalar()
    if exists:
        return False
    else:
        return True


def existsNumero(numero):
    exists = db.session.query(db.exists().where(
        Matriz.Matriz.numero == numero)).scalar()
    print(str(exists))
    if exists:
        return False
    else:
        return True


# def consultarMatrizRFID(rfid):  # Read
#     try:
#         matriz = db.session.query(
#             Matriz.Matriz.id).filter_by(rfid=rfid).first()
#         a = str(matriz).replace(", )", "")
#         id = str(a).replace("(", "")
#         return matriz[0]
#     except:
#         return False
