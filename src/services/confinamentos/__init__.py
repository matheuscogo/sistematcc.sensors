import responses
import requests
from requests.exceptions import ConnectionError

import json

# urlBase = "http://localhost:5000/api/v1/confinamentos/"
urlBase = "http://192.168.0.104:5000/api/v1/confinamentos/"



def getConfinamentoByMatriz(matrizId):
    try:
        resp = requests.get(f'{urlBase}getConfinamentoByMatriz/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
    

def getDaysInConfinament(matrizId):
    try:
        resp = requests.get(f'{urlBase}getDaysInConfinament/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]
    
def getQuantityForMatriz(matrizId):
    try:
        resp = requests.get(f'{urlBase}getQuantityForMatriz/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]
