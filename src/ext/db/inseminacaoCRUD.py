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


def cadastrarInseminacao(args):  # Create
    try:
        matrizId = int(args['matrizId'])
        planoId = int(args['planoId'])
        dataInseminacao = args['dataInseminacao']
        isNewCiclo = args['isNewCiclo']

        dataInseminacao = datetime.strftime(
            datetime.fromtimestamp(dataInseminacao/1000.0), '%d/%m/%y')

        if not matrizId:
            raise Exception(ResponseError)

        if not planoId:
            raise Exception(ResponseError)

        if not dataInseminacao:
            raise Exception(ResponseError)

        matriz = db.session.query(Matriz).filter_by(
            id=matrizId, deleted=False).first()
        inseminacao = db.session.query(Inseminacao).filter_by(
            matrizId=matrizId, active=True).first()
        confinamento = db.session.query(Confinamento).filter_by(
            matrizId=matrizId, active=True).first()

        if inseminacao:
            inseminacao.active = False
            inseminacao.deleted = True

        if confinamento:
            confinamento.active = False
            confinamento.deleted = True

        newConfinamento = Confinamento(
            planoId=planoId,
            matrizId=matrizId,
            dataConfinamento=dataInseminacao)

        db.session.add(newConfinamento)
        db.session.flush()

        print(newConfinamento.id)

        if isNewCiclo:
            matriz.ciclos = matriz.ciclos + 1

        newInseminacao = Inseminacao(
            planoId=planoId,
            matrizId=matrizId,
            dataInseminacao=dataInseminacao,
            confinamentoId=newConfinamento.id)
        # adicionar uma chave estrangeira na tabela inseminação para saber qual confinamento ela pertence
        db.session.add(newInseminacao)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Inseminacao cadastrado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
    finally:
        db.session.close()


def consultarInseminacoes():  # Read
    try:
        response = db.session.query(Inseminacao).filter_by(
            deleted=False, active=True).all()
        inseminacoes = []

        for inseminacao in response:
            matrizDescription = db.session.query(Matriz).filter_by(
                id=int(inseminacao.matrizId), deleted=False).first()
            planoDescription = db.session.query(Plano).filter_by(
                id=int(inseminacao.planoId), active=True, deleted=False).first()
            obj = {"id": inseminacao.id, "planoDescription": planoDescription.nome,
                   "matrizDescription": matrizDescription.rfid, "dataInseminacao": inseminacao.dataInseminacao}
            inseminacoes.append(obj)

        return inseminacoes
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def consultarInseminacao(id):  # Read
    try:
        inseminacao = db.session.query(Inseminacao).filter_by(id=id).first()
        return inseminacao
    except Exception as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def atualizarInseminacao(args):  # Update
    try:
        matriz = int(args['matriz'])
        dataInseminacao = str(args['dataInseminacao'])

        inseminacao = db.session.query(Inseminacao).filter_by(id=id).first()
        inseminacao.matrizId = matriz
        inseminacao.dataInseminacao = dataInseminacao
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Inseminacao atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirInseminacao(id):  # Delete
    try:
        inseminacao = db.session.query(Inseminacao).filter_by(id=id).first()
        db.session.delete(inseminacao)
        db.session.commit()
        return Response(response=json.dumps("{success: true, message: Inseminacao excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
