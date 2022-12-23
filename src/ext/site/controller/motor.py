from ext.config import sensors
from ext.site.controller import button
import time
from ...config import parametros


def init_app(GPIO):
    GPIO.setup(sensors.portaoAbrindo, GPIO.OUT)
    GPIO.setup(sensors.portaoFechando, GPIO.OUT)
    GPIO.setup(sensors.portaoSeparadorAbrindo, GPIO.OUT)
    GPIO.setup(sensors.portaoSeparadorFechando, GPIO.OUT)
    GPIO.setup(sensors.alimentador, GPIO.OUT)



def open(gpio):
    if button.closed(gpio):
        gpio.output(sensors.portaoAbrindo, 1)
        print("Abrindo portão....")
        while button.opened(gpio) is False:
            ...
        gpio.output(sensors.portaoAbrindo, 0)
        


def close(gpio):
    if button.opened(gpio):
        gpio.output(sensors.portaoFechando, 1)
        print("Fechando portão....")
        while button.closed(gpio) is False:
            ...
        gpio.output(sensors.portaoFechando, 0)


def openSeparador(gpio):
    while button.separadorClosed(gpio) is not True:
        gpio.output(sensors.portaoSeparadorFechando, 1)
        print("Fechando portão sepatrador....")

    gpio.output(sensors.portaoSeparadorFechando, 0)


def closeSeparador(gpio):
    while button.separadorOpened(gpio) is not True:
        gpio.output(sensors.portaoSeparadorAbrindo, 1)
        print("Abrindo portão separador....")

    gpio.output(sensors.portaoSeparadorAbrindo, 0)


def feed(matriz, gpio):
    print("Alimentando...")
    #gpio.output(sensors.alimentador, 1)

    matriz.quantidade = parametros.quantidadePorcao

    return matriz.quantidade
