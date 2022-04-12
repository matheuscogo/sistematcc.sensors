import responses
import requests
from requests.exceptions import ConnectionError

import json

# urlBase = "http://localhost:5000/api/v1/aviso/"
urlBase = "http://192.168.0.104:5000/api/v1/aviso/"

def insertAlert(addAviso):
    try:
        resp = requests.post(f'{urlBase}insert/', data=addAviso)

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]