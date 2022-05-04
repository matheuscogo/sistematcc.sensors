from services import confinamentos
from services import matrizes
from services import avisos
from services import registros
from services import dias

import RPi.GPIO as GPIO  # Importe la bibliothèque pour contrôler les GPIOs
import random
import time
import datetime

# Botão do sensor PIR
sensorPIR = 29

# Botão do portão principal(curso aberto)
cursoAbertura = 31  # porta1Aberta

# Botão do portão principal(curso fechado)
cursoFechamento = 33  # porta1Fechada

# Botão do portão separador(curso aberto)
cursoSepadorAbertura = 35  # porta2Aberta

# Botão do portão separador(curso fechado)
cursoSepadorFechamento = 37  # porta2Fechada

# Portão aberto(led verde)
portaoAberto = 36

# Portão fechado(led vermelho)
portaoFechado = 32

# Portão do separador aberto(led verde)
portaoSeparadorAberto = 40

# Portão do separador fechada(led vermelho)
portaoSeparadorFechado = 38

GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False)  # On désactive les messages d'alerte
GPIO.setup(sensorPIR, GPIO.IN)

GPIO.setup(cursoAbertura, GPIO.OUT)
GPIO.setup(cursoFechamento, GPIO.OUT)
GPIO.setup(cursoSepadorAbertura, GPIO.OUT)
GPIO.setup(cursoSepadorFechamento, GPIO.OUT)
GPIO.setup(portaoAberto, GPIO.OUT)
GPIO.setup(portaoFechado, GPIO.OUT)
GPIO.setup(portaoSeparadorAberto, GPIO.OUT)
GPIO.setup(portaoSeparadorFechado, GPIO.OUT)


def lerTag():  # retorna brinco aleatoriamente
    tag = ["123456789", "987654321"]
    r = random.randrange(0, 2, 1)  # inicia em 0 com 2 valores de 1 em 1 (0-1)
    return tag[r]


cursoAberturaControl = GPIO.input(cursoAbertura) == 1
cursoFechamentoControl = GPIO.input(cursoFechamento) == 1
cursoSepadorAberturaControl = GPIO.input(
    cursoSepadorAbertura) == 1
cursoSepadorFechamentoControl = GPIO.input(
    cursoSepadorFechamento) == 1


def start():
    fixarPIR = 0  # simular sensor PIR
    portao = 1  # porta 1 aberta (0 ou 1)
    separador = 1  # porta 2 aberta (0 ou 1)
    brinco = ''  # animal na maquina e brinco lido (1), sai da maquina (0)
    brincoLido = 0  # animal na maquina e brinco lido (1), sai da maquina (0)
    quantidadeTotal = 0

    print('Aperte botão sensorPIR (Ou saia com Ctrl + c): ')

    horaVeficada = datetime.datetime.today().hour
    GPIO.output(portaoAberto, 1)

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

    while True:
        # ==== So teste dos leds porta 2 ========
        if(GPIO.input(cursoSepadorFechamento) == 1):
            GPIO.output(portaoSeparadorFechado, 1)
            # print("Portão separador fechando...")
        else:
            GPIO.output(portaoSeparadorFechado, 0)

        if(GPIO.input(cursoSepadorAbertura) == 1):
            # print("Portão separador fechando...")
            GPIO.output(portaoSeparadorAberto, 1)
        else:
            GPIO.output(portaoSeparadorAberto, 0)

        if datetime.datetime.today().hour - horaVeficada > 24:
            confinamentos.verifyDaysToOpen()
            horaVeficada = datetime.datetime.today().hour

        if(GPIO.input(sensorPIR) == 1 or fixarPIR == 1):
            if(fixarPIR == 1 and GPIO.input(sensorPIR) == 0):
                time.sleep(0.5)
                # Simular que PIR não detectou presença
                fixarPIR = 0

            if(fixarPIR == 0 and GPIO.input(sensorPIR) == 1):
                time.sleep(0.5)
                # Simular que PIR esta detectando presença
                fixarPIR = 1

            # Fim de curso, portão fechado
            cursoAberturaControl = GPIO.input(cursoAbertura) == 1
            if cursoAberturaControl:
                GPIO.output(portaoFechado, 0)
                GPIO.output(portaoAberto, 0)

                print("Fechando portão...")
                time.sleep(5)

                # Fim de curso, portão fechado
                cursoFechamentoControl = GPIO.input(cursoFechamento) == 1
                if cursoFechamentoControl:
                    print("Portão fechado")
                    GPIO.output(portaoAberto, 0)
                    GPIO.output(portaoFechado, 1)
                    portao = 0  # porta 0 fechada

                    # enquanto brinco não lido ficar tentando ler
                    # brinco = None
                    brinco = lerTag()
                    print('Matriz {} identificada'.format(brinco))
                    brincoLido = brincoLido is None or '' in brinco

            if portao is 0 and fixarPIR is 1:
                if brincoLido:
                    matriz = matrizes.getMatrizByRfid(brinco)

                    if registro["dataEntrada"] is "":
                        registro['dataEntrada'] = datetime.datetime.now().strftime(
                            "%Y-%m-%d")

                    if registro["horaEntrada"] is "":
                        registro['horaEntrada'] = datetime.datetime.now().strftime(
                            "%H:%M:%S"
                        )

                    if registro["matrizId"] is 0:
                        registro['matrizId'] = matriz['id']

                    confinamento = confinamentos.getConfinamentoByMatriz(
                        matriz['id']
                    )

                    quantidade = int(confinamentos.getQuantityForMatriz(
                        matriz['id']
                    ))

                    podeSeparar = confinamentos.canOpenDoor(
                        matriz['id']
                    )

                    # dia = confinamentos.getDaysInConfinament(
                    #     matriz['id']
                    # )

                    # planoId = confinamento['planoId']

                    # controls = {
                    #     "planoId": planoId,
                    #     "dia": dia,
                    # }

                    # quantidadeDia = dias.consultarDia(controls)

                    verificarTotal = quantidadeTotal + 300

                    if(verificarTotal <= quantidade):
                        quantidadeTotal = quantidadeTotal + 300

                else:
                    verificaVezes += 1
                    if verificaVezes is 10:
                        # gerar aviso
                        verificaVezes = 0

        if podeSeparar:
            cursoSepadorFechamentoControl = GPIO.input(
                cursoSepadorFechamento) == 1

            if cursoSepadorFechamentoControl:
                print("Abrindo portão do separador...")
                time.sleep(5)

                cursoSepadorAberturaControl = GPIO.input(
                    cursoSepadorAbertura) == 1
                if cursoSepadorAberturaControl:
                    GPIO.output(portaoSeparadorAberto, 1)
                    GPIO.output(portaoSeparadorFechado, 0)
                    print("Portão separador aberto")

        if(fixarPIR == 0):
            brincoLido = 0
            brinco = ''

            cursoSepadorAberturaControl = GPIO.input(
                cursoSepadorAbertura) == 1
            if cursoSepadorAberturaControl:
                if podeSeparar:
                    print("Fechando porta do separador....")
                    time.sleep(5)

                    cursoSepadorFechamentoControl = GPIO.input(
                        cursoSepadorFechamento) == 1
                    if cursoSepadorFechamentoControl:
                        GPIO.output(portaoSeparadorAberto, 0)
                        GPIO.output(portaoSeparadorFechado, 1)
                        print("Portão separador fechado")

            cursoFechamentoControl = GPIO.input(cursoFechamento) == 1
            if cursoFechamentoControl:
                print("Abrindo portão...")
                time.sleep(5)

                cursoAberturaControl = GPIO.input(cursoAbertura) == 1
                # Fim de curso, e portão fechada
                if cursoAberturaControl:
                    GPIO.output(portaoAberto, 1)
                    GPIO.output(portaoFechado, 0)
                    print("Portão aberto")
                    portao = 1  # Portão aberto

                    registro['dataSaida'] = datetime.datetime.now().strftime(
                        "%Y-%m-%d")
                    registro['horaSaida'] = datetime.datetime.now().strftime(
                        "%H:%M:%S"
                    )

                    entrada = registro['dataEntrada'] + \
                        '' + registro['horaEntrada']
                    saida = registro['dataSaida'] + " " + registro['horaSaida']

                    horaEntrada = datetime.datetime.strptime(
                        registro['dataEntrada'] + ' ' +
                        registro['horaEntrada'], "%Y-%m-%d %H:%M:%S"
                    )

                    horaSaida = datetime.datetime.strptime(
                        registro['dataSaida'] + ' ' +
                        registro['horaSaida'], "%Y-%m-%d %H:%M:%S"
                    )

                    tempo = horaSaida - horaEntrada

                    registro['tempo'] = str(tempo.seconds)

                    registro['quantidade'] = quantidadeTotal

                    registros.insertRegistro(registro)

                    registro = {
                        "matrizId": 0,
                        "dataEntrada": "",
                        "dataSaida": "",
                        "horaEntrada": "",
                        "horaSaida": "",
                        "tempo": "",
                        "quantidade": 0
                    }

                    quantidadeTotal = 0


if __name__ == "__main__":
    start()
