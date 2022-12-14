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

    GPIO.output(sensors.portaoAbrindo, 0)
    GPIO.output(sensors.portaoFechando, 0)
    GPIO.output(sensors.portaoSeparadorAbrindo, 0)
    GPIO.output(sensors.portaoSeparadorFechando, 0)
    GPIO.output(sensors.alimentador, 0)





def open(gpio):
    open = button.opened(gpio)
    while open is not True:
        gpio.output(sensors.portaoAbrindo, 1)
        print("Abrindo portão....")

    gpio.output(sensors.portaoAbrindo, 0)


def close(gpio):
    close = button.closed(gpio)
    while close is not True:
        gpio.output(sensors.portaoFechando, 1)
        print("Fechando portão....")

    gpio.output(sensors.portaoFechando, 0)


def openSeparador(gpio):
    openSeparador = button.separadorClosed(gpio)
    while openSeparador is not True:
        gpio.output(sensors.portaoSeparadorFechando, 1)
        print("Fechando portão sepatrador....")

    gpio.output(sensors.portaoSeparadorFechando, 0)


def closeSeparador(gpio):
    closeSeparador = button.separadorOpened(gpio)
    while closeSeparador is not True:
        gpio.output(sensors.portaoSeparadorAbrindo, 1)
        print("Abrindo portão separador....")

    gpio.output(sensors.portaoSeparadorAbrindo, 0)


def feed(matriz, gpio):
    print("Alimentando...")
    gpio.output(sensors.alimentador, 1)
    time.sleep(parametros.intervaloPorções)
    gpio.output(sensors.alimentador, 0)

    matriz.quantidade = parametros.quantidadePorção

    return matriz.quantidade
