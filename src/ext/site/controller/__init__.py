from ext.site.model import Alimentador
from ext.site.model import Registro
from ext.site.controller import rfid
from ext.site.controller import button
from ext.site.controller import process
from ext.site.controller import pir
from ext.site.controller import motor
from datetime import datetime
import RPi.GPIO as GPIO

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

    start(GPIO)


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
