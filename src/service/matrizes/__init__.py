import responses
import requests
from requests.exceptions import ConnectionError

import json


def getMatrizByRfid(rfid):
    try:                  
        resp = requests.get(f'http://localhost:5000/api/v1/matrizesgetMatrizByRfid/'+str(rfid))

        if resp.ok is not True:
            raise ConnectionError("Error")
        
        teste = json.loads(resp.text)
        
        print(teste["id"])

        return json.loads(resp.text)
    
    except ConnectionError as ex:
        return ex.args[0]
