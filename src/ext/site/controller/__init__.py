from services import confinamentos
from services import matrizes
from services import avisos
from services import registros
from services import dias
from ext.site.model import Registro
from ext.site.model import Matriz
from ext.site.controller import rfid
from ext.site.controller import button
from ext.site.controller import pir
from ext.site.controller import motor
import random
import time
from datetime import datetime
from ext.config import sensors

import RPi.GPIO as GPIO  # Importe la bibliothèque pour contrôler les GPIOs
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

    leds()

    cursoAberturaControl = GPIO.input(sensors.cursoAbertura) == 1
    cursoFechamentoControl = GPIO.input(sensors.cursoFechamento) == 1
    cursoSepadorAberturaControl = GPIO.input(sensors.cursoSepadorAbertura) == 1
    cursoSepadorFechamentoControl = GPIO.input(
        sensors.cursoSepadorFechamento) == 1

    start(GPIO)


def start(gpio):
    fixarPIR = 0  # simular sensor PIR
    portao = 1  # porta 1 aberta (0 ou 1)
    separador = 0  # porta 2 aberta (0 ou 1)
    brinco = ''  # animal na maquina e brinco lido (1), sai da maquina (0)
    brincoLido = 0  # animal na maquina e brinco lido (1), sai da maquina (0)
    quantidadeTotal = 0

    print('Aperte botão sensorPIR (Ou saia com Ctrl + c): ')

    registro = {
        "matrizId": 0,
        "dataEntrada": "",
        "dataSaida": "",
        "horaEntrada": "",
        "horaSaida": "",
        "tempo": "",
        "quantidade": 0
    }

    verificaVezes = 0
    podeSeparar = False

    matrizReaded = None
    registro = None
    dataEntrada = None

    while True:
        try:
            if pir.read(gpio):
                if matrizReaded is None:
                    # matrizReaded = rfid.read()

                    if matrizReaded is None:
                        if dataEntrada is not None:
                            if datetime.now().second - dataEntrada.second > 30:
                                print("Matriz sem brinco aviso.")

                                registro = Registro(
                                    matrizId=matrizReaded.id,
                                    dataEntrada=datetime.now()
                                )
                        else:
                            dataEntrada = datetime.now()

                # registro = Registro(
                #     matrizId=matrizReaded.id,
                #     dataEntrada=datetime.now()
                # )

                if button.opened(gpio) and rfid.readed(matrizReaded):
                    motor.close(gpio)

                if button.closed(gpio) and rfid.readed(matrizReaded):
                    print("Inicio do processo.")

        except Exception as e:
            print(e.args[0])

        #     if(fixarPIR == 1 and gpio.input(sensors.sensorPIR) == 0):
        #         time.sleep(0.5)
        #         # Simular que PIR não detectou presença
        #         fixarPIR = 0

        #     if(fixarPIR == 0 and gpio.input(sensors.sensorPIR) == 1):
        #         time.sleep(0.5)
        #         # Simular que PIR esta detectando presença
        #         fixarPIR = 1

        #     if portao is 1:
        #         print("Fechando portão...")
        #         gpio.output(sensors.portaoFechando, 1)

        #     # Fim de curso, portão fechado
        #     cursoFechamentoControl = gpio.input(sensors.cursoFechamento) == 1
        #     if cursoFechamentoControl:
        #         gpio.output(sensors.portaoFechando, 0)
        #         print("Portão fechado")
        #         portao = 0  # porta 0 fechada

        #         # enquanto brinco não lido ficar tentando ler
        #         # brinco = None
        #         if brinco is '':
        #             brinco = rfid.read()
        #             print('Matriz {} identificada'.format(brinco))
        #             brincoLido = brincoLido is None or '' in brinco

        #     if portao is 0 and fixarPIR is 1:
        #         if brincoLido:
        #             matriz = matrizes.getMatrizByRfid(brinco)

        #             if registro["matrizId"] is 0:
        #                 registro['matrizId'] = matriz['id']

        #             if registro["dataEntrada"] is "":
        #                 registro['dataEntrada'] = datetime.datetime.now().strftime(
        #                     "%Y-%m-%d")

        #             if registro["horaEntrada"] is "":
        #                 registro['horaEntrada'] = datetime.datetime.now().strftime(
        #                     "%H:%M:%S"
        #                 )

        #             podeSeparar = confinamentos.canOpenDoor(
        #                 matriz['id']
        #             )

        #             quantidadeDia = int(confinamentos.getQuantityForMatriz(
        #                 matriz['id']
        #             ))

        #             time.sleep(10)
        #             if((quantidadeTotal + 300) <= quantidadeDia):
        #                 # Liberar comida
        #                 print("Liberando comida...")
        #                 quantidadeTotal = quantidadeTotal + 300

        #         else:
        #             verificaVezes += 1
        #             if verificaVezes is 10:
        #                 # gerar aviso
        #                 # Realizar a verificação por tempo
        #                 verificaVezes = 0

        # if podeSeparar:
        #     print("Abrindo portão do separador...")
        #     gpio.output(sensors.portaoSeparadorAbrindo, 1)

        #     cursoSepadorAberturaControl = gpio.input(
        #         sensors.cursoSepadorAbertura) == 1
        #     if cursoSepadorAberturaControl:
        #         gpio.output(sensors.portaoSeparadorAbrindo, 0)
        #         print("Portão separador aberto")
        #         separador = 1

        # if(fixarPIR == 0):
        #     brincoLido = 0
        #     brinco = ''

        #     registro['dataSaida'] = datetime.datetime.now().strftime(
        #         "%Y-%m-%d")
        #     registro['horaSaida'] = datetime.datetime.now().strftime(
        #         "%H:%M:%S")

        #     if separador is 1:
        #         print("Fechando porta do separador....")
        #         gpio.output(sensors.portaoSeparadorFechando, 1)

        #         cursoSepadorAberturaControl = gpio.input(
        #             sensors.cursoSepadorAbertura) == 1
        #         if cursoSepadorAberturaControl:
        #             gpio.output(sensors.portaoSeparadorFechando, 0)
        #             print("Portão separador fechado")
        #             separador = 0

        #     if portao is 0:
        #         print("Abrindo portão...")
        #         gpio.output(sensors.portaoAbrindo, 1)

        #         cursoAberturaControl = gpio.input(sensors.cursoAbertura) == 1
        #         # Fim de curso, e portão fechada
        #         if cursoAberturaControl:
        #             gpio.output(sensors.portaoAbrindo, 0)
        #             print("Portão aberto")

        #             horaEntrada = datetime.datetime.strptime(
        #                 registro['dataEntrada'] + ' ' +
        #                 registro['horaEntrada'], "%Y-%m-%d %H:%M:%S"
        #             )

        #             horaSaida = datetime.datetime.strptime(
        #                 registro['dataSaida'] + ' ' +
        #                 registro['horaSaida'], "%Y-%m-%d %H:%M:%S"
        #             )

        #             tempo = horaSaida - horaEntrada

        #             registro['tempo'] = str(tempo.seconds)

        #             registro['quantidade'] = quantidadeTotal

        #             registros.insertRegistro(registro)

        #             registro = {
        #                 "matrizId": 0,
        #                 "dataEntrada": "",
        #                 "dataSaida": "",
        #                 "horaEntrada": "",
        #                 "horaSaida": "",
        #                 "tempo": "",
        #                 "quantidade": 0
        #             }

        #             quantidadeTotal = 0

        #             portao = 1  # Portão aberto


def leds():
    # ==== So teste dos leds ======== #
    GPIO.output(sensors.portaoAbrindo, 1)
    time.sleep(0.3)
    GPIO.output(sensors.portaoAbrindo, 0)

    GPIO.output(sensors.portaoFechando, 1)
    time.sleep(0.3)
    GPIO.output(sensors.portaoFechando, 0)

    GPIO.output(sensors.portaoSeparadorAbrindo, 1)
    time.sleep(0.3)
    GPIO.output(sensors.portaoSeparadorAbrindo, 0)

    GPIO.output(sensors.portaoSeparadorFechando, 1)
    time.sleep(0.3)
    GPIO.output(sensors.portaoSeparadorFechando, 0)
