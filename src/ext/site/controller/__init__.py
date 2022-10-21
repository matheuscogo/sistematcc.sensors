from ext.site.model import Alimentador
from ext.site.model import Registro
from ext.site.controller import rfid
from ext.site.controller import button
from ext.site.controller import process
from ext.site.controller import pir
from ext.site.controller import motor
from datetime import datetime
import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial("/dev/serial0", 115200)

GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False)  # On désactive les messages d'alerte


cursoAberturaControl = False
cursoFechamentoControl = False
cursoSepadorAberturaControl = False
cursoSepadorFechamentoControl = False


def init_app():
    rfid.init_app(GPIO)
    button.init_app(GPIO)
    pir.init_app(GPIO)
    motor.init_app(GPIO)

    rfidTest()
    buttonTest()
    motorTest()
    pirTest()

    # start(GPIO)


def start(gpio):
    print('Sistema iniciado, aguardando sensorPIR (Ou saia com Ctrl + c): ')

    matrizReaded = None
    registro = None
    entrada = None
    saida = None

    while True:
        try:
            if pir.read(gpio):
                if matrizReaded is None:
                    matrizReaded = rfid.read()

                if entrada is None and matrizReaded is None:
                    entrada = datetime.now()

                if entrada is not None:
                    if (datetime.now() - entrada).seconds > 30:
                        print("Matriz sem brinco aviso.")

                if matrizReaded is not None:
                    if matrizReaded.quantidade <= matrizReaded.quantidadeTotal:
                        alimentador = Alimentador(
                            matrizId=matrizReaded.id,
                            dataEntrada=matrizReaded.entrada,
                            quantidade=matrizReaded.quantidade+300,
                            confinamentoId=matrizReaded.confinamento.id,
                            planoId=matrizReaded.confinamento.planoId,
                            hash=matrizReaded.hash,
                        )

                        matrizReaded.quantidade = motor.feed(alimentador)

            elif not pir.read(gpio) and matrizReaded is not None:
                saida = datetime.now()

                if (datetime.now() - saida).seconds > 30 and button.closed(gpio):
                    register = process.query(matrizReaded.hash)
                    registro = Registro(
                        matrizId=register.matrizId,
                        dataEntrada=matrizReaded.entrada,
                        dataSaida=datetime.now(),
                        tempo=(datetime.now() - matrizReaded.entrada).seconds,
                        quantidade=register.quantidadeTotal,
                    )

                    # Salva os dados no banco e abre a porta
                    print("Salvando os dados....")
                    process.save(registro)
                    clean()
                    motor.open(gpio)

        except Exception as e:
            print(e.args[0])


def clean():
    matrizReaded = None
    registro = None
    entrada = None
    saida = None


def buttonTest():
    cursoSepadorFechamento = GPIO.input(31) == 1
    cursoSepadorAbertura = GPIO.input(33) == 1
    cursoFechamento = GPIO.input(35) == 1
    cursoAbertura = GPIO.input(37) == 1

    if cursoAbertura:
        print("Botão curso abertura")

    if cursoFechamento:
        print("Botão curso fechamento")

    if cursoSepadorAbertura:
        print("Botão curso separador abertura")

    if cursoSepadorFechamento:
        print("Botão curso separador fechamento")


def motorTest():
    GPIO.output(32, 1)
    time(0.5)
    GPIO.output(32, 0)

    GPIO.output(36, 1)
    time(0.5)
    GPIO.output(36, 0)

    GPIO.output(40, 1)
    time(0.5)
    GPIO.output(40, 0)

    GPIO.output(38, 1)
    time(0.5)
    GPIO.output(38, 0)


def pirTest():
    if GPIO.input(29) == 1:
        print("Há presença na maquina")
    else:
        print("Não há presença na maquina")


def rfidTest():
    if ser.inWaiting() > 0:
        tag = ser.readline()
        tag = tag.decode("utf-8")  # bytes para str
        tag = tag.rstrip()

        print("Tag:" + tag)
    else:
        print("Tag não recebida")
