from datetime import datetime
from ext.config import sensors
from ext.site.controller import button
from ext.db import alimentadorCRUD
import time
from ...config import parametros

def init_app(GPIO):
    GPIO.setup(sensors.portaoAbrindo, GPIO.OUT)
    GPIO.setup(sensors.portaoFechando, GPIO.OUT)
    GPIO.setup(sensors.portaoSeparadorAbrindo, GPIO.OUT)
    GPIO.setup(sensors.portaoSeparadorFechando, GPIO.OUT)

    GPIO.output(sensors.portaoAbrindo, 0)
    GPIO.output(sensors.portaoFechando, 0)
    GPIO.output(sensors.portaoSeparadorAbrindo, 0)
    GPIO.output(sensors.portaoSeparadorFechando, 0)


def open(gpio):
    while button.opened(gpio) is not True:
        gpio.output(sensors.portaoAbrindo, 1)
        print("Abrindo portão....")

    gpio.output(sensors.portaoAbrindo, 0)


def close(gpio):
    while button.closed(gpio) is not True:
        gpio.output(sensors.portaoFechando, 1)
        print("Fechando portão....")

    gpio.output(sensors.portaoFechando, 0)


def closeSeparador(gpio):
    while button.separadorOpened(gpio) is not True:
        gpio.output(sensors.portaoSeparadorAbrindo, 1)
        print("Abrindo portão separador....")

    gpio.output(sensors.portaoSeparadorAbrindo, 0)


def openSeparador(gpio):
    while button.separadorClosed(gpio) is not True:
        gpio.output(sensors.portaoSeparadorFechando, 1)
        print("Fechando portão sepatrador....")

    gpio.output(sensors.portaoSeparadorFechando, 0)


def feed(alimentador, gpio):
    print("Alimentando...")
    gpio.output(sensors.alimentador, 1)
    time.sleep(parametros.intervaloPorções)
    gpio.output(sensors.alimentador, 0)
    
    alimentador.quantidade = parametros.quantidadePorção

    alimentadorCRUD.cadastrarAlimentador(alimentador)
    return alimentador.quantidade
