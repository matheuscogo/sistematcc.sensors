import responses
import requests
from requests.exceptions import ConnectionError

import json

# urlBase = "http://localhost:5000/api/v1/dias/"
urlBase = "http://192.168.0.104:5000/api/v1/dias/"


def consultarDia(controls):
    try:
        dia = str(controls['dia'])
        planoId = str(controls['planoId'])

        resp = requests.get(f'{urlBase}/' + dia + '/' + planoId)

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]
