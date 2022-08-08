from services import registros
from ext.site.model import Registro
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


def consultarRegistros():  # Read
    try:
        # registros = db.session.query(Registro.Registro).all()
        if not registros:
            raise BaseException("Erro ao consultar no banco de dados")
        return registros
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


def atualizarRegistro(args):  # Update
    try:
        id = int(args['id'])
        matriz = int(args['matriz'])
        dataEntrada = str(args['dataEntrada'])
        dataSaida = str(args['dataSaida'])
        horaEntrada = str(args['horaEntrada'])
        horaSaida = str(args['horaSaida'])
        tempo = str(args['tempo'])
        quantidade = int(args['quantidade'])

        registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        registro.matriz = matriz
        registro.dataEntrada = dataEntrada
        registro.dataSaida = dataSaida
        registro.horaEntrada = horaEntrada
        registro.horaSaida = horaSaida
        registro.tempo = tempo
        registro.quantidade = quantidade
        # db.session.commit()
        return Response(response=json.dumps("{success: true, message: Registro atualizado com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)


def excluirRegistro(id):  # Delete
    try:
        # registro = db.session.query(Registro.Registro).filter_by(id=id).first()
        # db.session.delete(registro)
        # db.session.commit()
        return Response(response=json.dumps("{success: true, message: Registro excluido com sucesso!, response: null}"), status=200)
    except BaseException as e:
        return Response(response=json.dumps("{success: false, message: " + e.args[0] + ", response: null}"), status=501)
