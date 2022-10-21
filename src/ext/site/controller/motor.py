from datetime import datetime
from ext.config import sensors
from ext.site.controller import button
from ext.db import alimentadorCRUD


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


def feed(alimentador):
    alimentadorCRUD.cadastrarAlimentador(alimentador)
    print("Alimentando...")
    return alimentador.quantidade


def porta(acao):
    # TODO -> Abrir ou fechar motor

    # TODO -> ABRIR
    # Se ação for abrir e o botão aberto não foi precionado
    # Mandar abrir
    # Se o botão aberto for precionado
    # Para de abrir

    # TODO -> FECHAR
    # Se ação for fechar e o botão fechar não foi precionado
    # Mandar fechar
    # Se o botão fechado for precionado
    # Para de fechar
    ...


def separador(acao):
    # TODO -> Abrir ou fechar motor

    # TODO -> ABRIR
    # Se ação for abrir
    # Mandar abrir
    # Se o botão aberto for precionado
    # Para de abrir

    # TODO -> FECHAR
    # Se ação for fechar
    # Mandar fechar
    # Se o botão fechado for precionado
    # Para de fechar
    ...


def alimentador(matriz):
    # TODO -> Função ligar ou desligar motor do alimentador

    # Variavel porçãoDia

    # Se matriz não foi identificada, chamar quantidade de ração definida nos parametros
    # Define porçãoDia

    # Consulta a porãoDia menos a quantidade registrada naquele dia(tabela registros)
    # Enquanto matriz está dentro do alimentador
    # Equanto porçãoDia for maior que a porçãoAtual -> alimentar a matriz
    # Ligar motor
    # time.sleep(consultar tempo do motor dos parametros)
    # Desligar motor
    # Somar a porçãoAtual de ração que ainda resta com base na quantidade por tempo definada pela tabela de parametros

    # Na saida do looping -> salvar dados na tabela registros
    ...
