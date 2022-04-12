import responses
import requests
from requests.exceptions import ConnectionError

import json

# urlBase = "http://localhost:5000/api/v1/matrizes/"
urlBase = "http://192.168.0.104:5000/api/v1/matrizes/"


def getMatrizByRfid(rfid):
    try:
        resp = requests.get(f'{urlBase}getMatrizByRfid/'+str(rfid))

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        teste = json.loads(resp.text)
        
        print(teste["id"])

        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
