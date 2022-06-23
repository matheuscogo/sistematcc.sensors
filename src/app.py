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

# Portão abrindo(led verde)
portaoAbrindo = 36

# Portão fechando(led vermelho)
portaoFechando = 32

# Portão do separador abrindo(led verde)
portaoSeparadorAbrindo = 40

# Portão do separador fechando(led vermelho)
portaoSeparadorFechando = 38

GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False)  # On désactive les messages d'alerte
GPIO.setup(sensorPIR, GPIO.IN)

GPIO.setup(cursoAbertura, GPIO.OUT)
GPIO.setup(cursoFechamento, GPIO.OUT)
GPIO.setup(cursoSepadorAbertura, GPIO.OUT)
GPIO.setup(cursoSepadorFechamento, GPIO.OUT)
GPIO.setup(portaoAbrindo, GPIO.OUT)
GPIO.setup(portaoFechando, GPIO.OUT)
GPIO.setup(portaoSeparadorAbrindo, GPIO.OUT)
GPIO.setup(portaoSeparadorFechando, GPIO.OUT)


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
    separador = 0  # porta 2 aberta (0 ou 1)
    brinco = ''  # animal na maquina e brinco lido (1), sai da maquina (0)
    brincoLido = 0  # animal na maquina e brinco lido (1), sai da maquina (0)
    quantidadeTotal = 0

    print('Aperte botão sensorPIR (Ou saia com Ctrl + c): ')

    horaVeficada = datetime.datetime.today().hour

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
            GPIO.output(portaoSeparadorFechando, 1)
            # print("Portão separador fechando...")
        else:
            GPIO.output(portaoSeparadorFechando, 0)

        if(GPIO.input(cursoSepadorAbertura) == 1):
            # print("Portão separador fechando...")
            GPIO.output(portaoSeparadorAbrindo, 1)
        else:
            GPIO.output(portaoSeparadorAbrindo, 0)

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

            if portao is 1:
                print("Fechando portão...")
                GPIO.output(portaoFechando, 1)

            # Fim de curso, portão fechado
            cursoFechamentoControl = GPIO.input(cursoFechamento) == 1
            if cursoFechamentoControl:
                GPIO.output(portaoFechando, 0)
                print("Portão fechado")
                portao = 0  # porta 0 fechada

                # enquanto brinco não lido ficar tentando ler
                # brinco = None
                if brinco is '':
                    brinco = lerTag()
                    print('Matriz {} identificada'.format(brinco))
                    brincoLido = brincoLido is None or '' in brinco

            if portao is 0 and fixarPIR is 1:
                if brincoLido:
                    matriz = matrizes.getMatrizByRfid(brinco)

                    if registro["matrizId"] is 0:
                        registro['matrizId'] = matriz['id']

                    if registro["dataEntrada"] is "":
                        registro['dataEntrada'] = datetime.datetime.now().strftime(
                            "%Y-%m-%d")

                    if registro["horaEntrada"] is "":
                        registro['horaEntrada'] = datetime.datetime.now().strftime(
                            "%H:%M:%S"
                        )

                    podeSeparar = confinamentos.canOpenDoor(
                        matriz['id']
                    )

                    quantidadeDia = int(confinamentos.getQuantityForMatriz(
                        matriz['id']
                    ))

                    time.sleep(10)
                    if((quantidadeTotal + 300) <= quantidadeDia):
                        # Liberar comida
                        print("Liberando comida...")
                        quantidadeTotal = quantidadeTotal + 300

                else:
                    verificaVezes += 1
                    if verificaVezes is 10:
                        # gerar aviso
                        # Realizar a verificação por tempo
                        verificaVezes = 0

        if podeSeparar:
            print("Abrindo portão do separador...")
            GPIO.output(portaoSeparadorAbrindo, 1)

            cursoSepadorAberturaControl = GPIO.input(
                cursoSepadorAbertura) == 1
            if cursoSepadorAberturaControl:
                GPIO.output(portaoSeparadorAbrindo, 0)
                print("Portão separador aberto")
                separador = 1

        if(fixarPIR == 0):
            brincoLido = 0
            brinco = ''

            registro['dataSaida'] = datetime.datetime.now().strftime(
                "%Y-%m-%d")
            registro['horaSaida'] = datetime.datetime.now().strftime(
                "%H:%M:%S")

            if separador is 1:
                print("Fechando porta do separador....")
                GPIO.output(portaoSeparadorFechando, 1)

                cursoSepadorAberturaControl = GPIO.input(
                    cursoSepadorAbertura) == 1
                if cursoSepadorAberturaControl:
                    GPIO.output(portaoSeparadorFechando, 0)
                    print("Portão separador fechado")
                    separador = 0

            if portao is 0:
                print("Abrindo portão...")
                GPIO.output(portaoAbrindo, 1)

                cursoAberturaControl = GPIO.input(cursoAbertura) == 1
                # Fim de curso, e portão fechada
                if cursoAberturaControl:
                    GPIO.output(portaoAbrindo, 0)
                    print("Portão aberto")

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

                    portao = 1  # Portão aberto


if __name__ == "__main__":
    start()
