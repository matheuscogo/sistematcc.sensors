import responses
import requests
from requests.exceptions import ConnectionError

import json

# urlBase = "http://localhost:5000/api/v1/registros/"
urlBase = "http://192.168.0.104:5000/api/v1/registros/"


def getMatrizByRfid(registro):
    try:
        resp = requests.post(f'{urlBase}insert/', data=registro)

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        teste = json.loads(resp.text)
        
        print(teste["id"])

        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
