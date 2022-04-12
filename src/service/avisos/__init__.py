import responses
import requests
from requests.exceptions import ConnectionError

import json

def insertAlert(addAviso):
    try:
        resp = requests.post(f'http://localhost:5000/api/v1/aviso/insert/', data=addAviso)

        if resp.ok is not True:
            raise ConnectionError("Error")

        return json.loads(resp.text)
    except ConnectionError as ex:
        return ex.args[0]