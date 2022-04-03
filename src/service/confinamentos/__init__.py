from asyncio import exceptions
import responses
import requests
from requests.exceptions import ConnectionError

import json


def getConfinamentoByMatriz(matrizId):
    try:                  
        resp = requests.get(f'http://localhost:5000/api/v1/confinamentos/getConfinamentoByMatriz/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        teste = json.loads(resp.text)
        
        print(teste["id"])

        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
