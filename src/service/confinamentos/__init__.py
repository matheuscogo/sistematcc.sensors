import responses
import requests
from requests.exceptions import ConnectionError

import json


def getConfinamentoByMatriz(matrizId):
    try:                  
        resp = requests.get(f'http://localhost:5000/api/v1/confinamentos/getConfinamentoByMatriz/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
    

def getDaysInConfinament(matrizId):
    try:                  
        resp = requests.get(f'http://localhost:5000/api/v1/confinamentos/getDaysInConfinament/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]
    
def getQuantityForMatriz(matrizId):
    try:                  
        resp = requests.get(f'http://localhost:5000/api/v1/confinamentos/getQuantityForMatriz/'+str(matrizId))

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]

def insertAlert(addAviso):
    try:                  
        resp = requests.post(f'http://localhost:5000/api/v1/aviso/insert/', data=addAviso)

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]
