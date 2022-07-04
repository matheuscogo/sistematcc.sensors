from ..site.model import Matriz
from ..db import session
from werkzeug.wrappers import Response, Request
import json


def cadastrarMatriz(args):  # Create
    try:
        numero = str(args['numero'])
        rfid = str(args['rfid'])
        ciclos = str(args['ciclos'])
        db.session.add(Matriz.Matriz(rfid=rfid, numero=numero, ciclos=ciclos))
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Matriz cadastrada com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarMatrizes():  # Read
    try:
        matrizes = db.session.query(Matriz.Matriz).all()
        return matrizes
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
