import random
from ext.config import sensors
from ext.db import matrizCRUD
from datetime import datetime

readDate = None


def init_app(GPIO):
    # GPIO.setup(sensors.sensorPIR, GPIO.IN)
    # GPIO.setup(sensors.cursoAbertura, GPIO.OUT)
    # GPIO.setup(sensors.cursoFechamento, GPIO.OUT)
    # GPIO.setup(sensors.cursoSepadorAbertura, GPIO.OUT)
    # GPIO.setup(sensors.cursoSepadorFechamento, GPIO.OUT)
    # GPIO.setup(sensors.portaoAbrindo, GPIO.OUT)
    # GPIO.setup(sensors.portaoFechando, GPIO.OUT)
    # GPIO.setup(sensors.portaoSeparadorAbrindo, GPIO.OUT)
    # GPIO.setup(sensors.portaoSeparadorFechando, GPIO.OUT)
    ...


def read():  # retorna brinco aleatoriamente
    tag = ["123456789", "987654321"]
    r = random.randrange(0, 2, 1)  # inicia em 0 com 2 valores de 1 em 1 (0-1)
    brinco = tag[0]
    matriz = matrizCRUD.consultarMatrizRFID(brinco)
    print('Matriz {} identificada'.format(matriz.rfid))

    if matriz is not None:
        return matriz

    return None


def readed(matriz):  # retorna brinco aleatoriamente
    return matriz is not None
