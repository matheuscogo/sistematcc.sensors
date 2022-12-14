from ..site.model.Parametro import Parametro
from ..db import session
from ..config import parametros


def consultarParametros():  # Read
    try:
        param = session.query(Parametro).first()

        if param != None:
            parametros.tempoPorcao = param.tempoPorcao
            parametros.quantidadePorcao = param.quantidadePorcao
            parametros.intervaloPorcoes = param.intervaloPorcoes
            parametros.tempoProximaMatriz = param.tempoProximaMatriz

        response = {
            "success": True,
            "response": parametros,
            "message": ""
        }

        return response
    except Exception as e:
        response = {
            'success': False,
            'response': {},
            'message': e.args[0]
        }

        return response
