from services import confinamentos
from services import matrizes
from services import avisos

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import random
import time
import datetime

#Botão do sensor PIR
sensorPIR=29

#Botão do portão principal(curso aberto)
cursoAbertura=31 #porta1Aberta

#Botão do portão principal(curso fechado)
cursoFechamento=33 #porta1Fechada

#Botão do portão separador(curso aberto)
cursoSepadorAbertura=35 #porta2Aberta

#Botão do portão separador(curso fechado)
cursoSepadorFechamento=37 #porta2Fechada

#Portão aberto(led verde)
portaoAberto=36

#Portão fechado(led vermelho)
portaoFechado=32

#Portão do separador aberto(led verde)
portaoSeparadorAberto=40

#Portão do separador fechada(led vermelho)
portaoSeparadorFechado=38

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte
GPIO.setup(sensorPIR,GPIO.IN)

GPIO.setup(cursoAbertura,GPIO.OUT)
GPIO.setup(cursoFechamento,GPIO.OUT)
GPIO.setup(cursoSepadorAbertura,GPIO.OUT)
GPIO.setup(cursoSepadorFechamento,GPIO.OUT)
GPIO.setup(portaoAberto,GPIO.OUT)
GPIO.setup(portaoFechado,GPIO.OUT)
GPIO.setup(portaoSeparadorAberto,GPIO.OUT)
GPIO.setup(portaoSeparadorFechado,GPIO.OUT)

def lerTag():  # retorna brinco aleatoriamente 
    tag=["123456789","987654321"]
    r=random.randrange(0, 2, 1) # inicia em 0 com 2 valores de 1 em 1 (0-1)
    return tag[r]

def start():
    fixarPIR=0 # simular sensor PIR
    portao=1 # porta 1 aberta (0 ou 1)
    separador=1 # porta 2 aberta (0 ou 1)
    brincoLido=0 # animal na maquina e brinco lido (1), sai da maquina (0) 
    
    print('Aperte botão sensorPIR (Ou saia com Ctrl + c): ')

    horaVeficada = datetime.datetime.today().hour
    GPIO.output(portaoAberto,1)

    while True:
# ==== So teste dos leds porta 2 ========
        if(GPIO.input(cursoSepadorFechamento) == 1):
            GPIO.output(portaoSeparadorFechado,1)
            # print("Portão separador fechando...")
        else:
            GPIO.output(portaoSeparadorFechado,0)
        
        if(GPIO.input(cursoSepadorAbertura) == 1):
            # print("Portão separador fechando...")
            GPIO.output(portaoSeparadorAberto,1)
        else:
            GPIO.output(portaoSeparadorAberto,0)
        
        if datetime.datetime.today().hour - horaVeficada  > 24:
            confinamentos.verifyDaysToOpen()
            horaVeficada = datetime.datetime.today().hour

        if(GPIO.input(sensorPIR) == 1 or fixarPIR == 1):
            if(fixarPIR == 0 and GPIO.input(sensorPIR) == 1):
                time.sleep(0.5)
                # Simular que PIR esta detectando presença
                fixarPIR = 1

            if(fixarPIR == 1 and GPIO.input(sensorPIR) == 1):
                time.sleep(0.5)
                # Simular que PIR não detectou presença
                fixarPIR = 0
        
            # Se portão estiver aberto, então fechar
            if(portao==1):
                GPIO.output(portaoFechado,0)
                GPIO.output(portaoAberto,0)
                print("Fechando portão...")
            
                # Fim de curso portão fechado
                if(GPIO.input(cursoAbertura) == 1):
                    print("Portão fechado")
                    GPIO.output(portaoAberto,0)
                    GPIO.output(portaoFechado,1)
                    portao=0; # porta 1 fechada

                    # enquanto brinco não lido ficar tentando ler
                    if(not brincoLido):
                        brinco=lerTag()
                
                        matriz = matrizes.getMatrizByRfid(brinco)
                        confinamento = confinamentos.getConfinamentoByMatriz(matriz['id'])
                
                        quantidade = confinamentos.getQuantityForMatriz(matriz['id'])
                
                        brincoLido=1    
                        print ('Matriz {} identificada'.format(brinco))
                    
        if(fixarPIR == 0):
            brincoLido=0

            # Se portão fechado, então abrir
            if(portao==0):
                GPIO.output(portaoAberto,0)
                GPIO.output(portaoFechado,0)
                print("Abrindo portão...")

                # Fim de curso e portão fechada
                if(GPIO.input(cursoFechamento) == 1):
                    GPIO.output(portaoAberto,1)
                    print("Portão aberto")
                    portao=1 # Portão aberto


if __name__ == "__main__":
    start()
