from ext.site.model import Registro
from ext.db import avisoCRUD, parametroCRUD
from ext.site.controller import rfid
from ext.site.controller import button
from ext.site.controller import process
from ext.site.controller import pir
from ext.site.controller import motor
from datetime import datetime, timedelta
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
    tempoSemLeitura = None
    saida = None
    tempoAlimentadorLigado = None
    ultimaPorcao = None

    parametroCRUD.consultarParametros()

    while True:
        try:
            if pir.read(gpio):
                # Se matriz detectada, zera a saida que controla o tempo sem matriz
                saida = None
                if matrizReaded is None:
                    # Retorna os dados da matriz, qual matriz é, quantidade,
                    # data entrada, entre outros dados
                    matrizReaded = rfid.read(gpio)
                    tempoSemLeitura = None

                if tempoSemLeitura is None and matrizReaded is None:
                    tempoSemLeitura = datetime.now()

                if tempoSemLeitura is not None:
                    if (datetime.now() - tempoSemLeitura).seconds > parametros.tempoSemBrinco:
                        print("Matriz sem brinco")
                        avisoCRUD.cadastrarAviso(
                            confinamentoId=matrizReaded.confinamento.id,
                            type=1
                        )
                        
                # Se matriz não está vazia, verifica se o alimentador está ligado, se desligado
                # verifica se a matriz pode comer ainda, se pode liga o motor do alimentador e zera
                # a contagem do intervalo
                if matrizReaded is not None:
                    if tempoAlimentadorLigado is None:
                        if matrizReaded.quantidade < matrizReaded.quantidadeTotal:
                            if ultimaPorcao is None:
                                ultimaPorcao = datetime.now() - timedelta(days=1)
                                
                            if (datetime.now() - ultimaPorcao).seconds > parametros.intervaloPorcoes:
                                ultimaPorcao = datetime.now()
                                tempoAlimentadorLigado = datetime.now()
                                matrizReaded.quantidade += motor.feed(matrizReaded, gpio)

                if tempoAlimentadorLigado is not None:
                    if (datetime.now() - tempoAlimentadorLigado).seconds > parametros.tempoPorcao:
                        gpio.output(sensors.alimentador, 0)
                        tempoAlimentadorLigado = None
                        ultimaPorcao = datetime.now()

                     
            # Controla tempo sem presença
            elif not pir.read(gpio):
                if saida is None:
                    saida = datetime.now()

                # Tempo para desligar o alimentador caso não haja detecção da matriz
                if tempoAlimentadorLigado is not None:
                    if (datetime.now() - tempoAlimentadorLigado).seconds > 10:
                        gpio.output(sensors.alimentador, 0)
                        tempoAlimentadorLigado = None
                
                # Verificação para finalizar o processo, abrindo as portas
                # salvando os dados no banco e limpando os dados globais
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
                        matrizReaded = None
                        registro = None
                        tempoSemLeitura = None
                        saida = None
                        tempoAlimentadorLigado = None
                        ultimaPorcao = None

                    motor.open(gpio)
                    motor.closeSeparador(gpio)

        except Exception as e:
            print(e.args[0])


def clean():
    matrizReaded = None
    registro = None
    entrada = None
    saida = None
