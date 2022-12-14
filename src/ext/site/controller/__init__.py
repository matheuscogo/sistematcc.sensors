from ext.site.model import Registro
from ext.db import avisoCRUD, parametroCRUD
from ext.site.controller import rfid
from ext.site.controller import button
from ext.site.controller import process
from ext.site.controller import pir
from ext.site.controller import motor
from datetime import datetime
from ...config import parametros
import RPi.GPIO as GPIO
from ...config import sensors

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


cursoAberturaControl = False
cursoFechamentoControl = False
cursoSepadorAberturaControl = False
cursoSepadorFechamentoControl = False


def init_app():
    rfid.init_app(GPIO)
    button.init_app(GPIO)
    pir.init_app(GPIO)
    motor.init_app(GPIO)

    GPIO.output(sensors.portaoAbrindo, 0)
    GPIO.output(sensors.portaoFechando, 0)
    GPIO.output(sensors.portaoSeparadorAbrindo, 0)
    GPIO.output(sensors.portaoSeparadorFechando, 0)
    GPIO.output(sensors.alimentador, 0)

    motor.open(GPIO)
    motor.closeSeparador(GPIO)

    start(GPIO)


def start(gpio):
    print('Sistema iniciado, aguardando sensorPIR (Ou saia com Ctrl + c): ')

    matrizReaded = None
    registro = None
    entrada = None
    saida = None

    parametroCRUD.consultarParametros()

    while True:
        try:
            if pir.read(gpio):
                saida = None
                if matrizReaded is None:
                    matrizReaded = rfid.read(gpio)

                if entrada is None and matrizReaded is None:
                    entrada = datetime.now()

                if entrada is not None:
                    if (datetime.now() - entrada).seconds > parametros.tempoSemBrinco:
                        print("Matriz sem brinco")
                        avisoCRUD.cadastrarAviso(
                            confinamentoId=matrizReaded.confinamento.id,
                            type=1
                        )

                if matrizReaded is not None:
                    if matrizReaded.quantidade <= matrizReaded.quantidadeTotal:
                        matrizReaded.quantidade += motor.feed(matrizReaded, gpio)

            elif not pir.read(gpio):
                if saida is None:
                    saida = datetime.now()

                if (datetime.now() - saida).seconds > parametros.tempoProximaMatriz and button.closed(gpio):
                    if matrizReaded is not None:
                        registro = Registro(
                            confinamentoId=matrizReaded.confinamentoId[0],
                            dataEntrada=matrizReaded.entrada,
                            dataSaida=datetime.now(),
                            quantidade=matrizReaded.quantidade,
                        )

                        # Salva os dados no banco e abre a porta
                        print("Salvando os dados....")
                        process.save(registro)
                        clean()

                    motor.open(gpio)
                    motor.closeSeparador(gpio)

        except Exception as e:
            print(e.args[0])


def clean():
    matrizReaded = None
    registro = None
    entrada = None
    saida = None
