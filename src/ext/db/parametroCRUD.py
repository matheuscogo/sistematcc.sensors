from ..site.model.Parametro import Parametro
from ..db import session
from ..config import parametros


def consultarParametros():  # Read
    try:
        param = session.query(Parametro).first()

        if param != None:
            parametros.tempoPorção = param.tempoPorção
            parametros.quantidadePorção = param.quantidadePorção
            parametros.intervaloPorções = param.intervaloPorções
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
