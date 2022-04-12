from services import confinamentos
from services import matrizes
from services import avisos

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import random
import time
import datetime

sensorPIR=29
porta1Fechada=31
porta1Aberta=33
porta2Fechada=35
porta2Aberta=37

porta1Fechando=32
porta1Abrindo=36
porta2Fechando=38
porta2Abrindo=40

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte
GPIO.setup(sensorPIR,GPIO.IN)

GPIO.setup(porta1Fechada,GPIO.OUT)
GPIO.setup(porta2Fechada,GPIO.OUT)
GPIO.setup(porta1Aberta,GPIO.OUT)
GPIO.setup(porta2Aberta,GPIO.OUT)
GPIO.setup(porta1Fechando,GPIO.OUT)
GPIO.setup(porta1Abrindo,GPIO.OUT)
GPIO.setup(porta2Fechando,GPIO.OUT)
GPIO.setup(porta2Abrindo,GPIO.OUT)

def lerTag():  # retorna brinco aleatoriamente 
    tag=["123456789","987654321"]
    r=random.randrange(0, 2, 1) # inicia em 0 com 2 valores de 1 em 1 (0-1)
    return tag[r]

def start():
    fixarPIR=0 # simular sensor PIR
    P1=1 # porta 1 aberta (0 ou 1)
    P2=1 # porta 2 aberta (0 ou 1)
    brincoLido=0 # animal na maquina e brinco lido (1), sai da maquina (0) 
    
    print('Aperte botão sensorPIR (Ou saia com Ctrl + c): ')

    horaVeficada = datetime.datetime.today().hour
    #On va faire une boucle infinie pour lire en boucle
    while True:

# ==== So teste dos leds porta 2 ========
        if(GPIO.input(porta2Fechada) == 1):
            print("2fechada")
            GPIO.output(porta2Fechando,1)
        else:
            GPIO.output(porta2Fechando,0)
        
        
        if(GPIO.input(porta2Aberta) == 1):
            print("2aberta")
            GPIO.output(porta2Abrindo,1)
        else:
            GPIO.output(porta2Abrindo,0)

        data = datetime.datetime.today().hour - horaVeficada
        
        if datetime.datetime.today().hour - horaVeficada  > 24:
            confinamentos.verifyDaysToOpen()
            horaVeficada = datetime.datetime.today().hour
    # ========================================    

        if(GPIO.input(sensorPIR) == 1 or fixarPIR == 1 ):
            if(fixarPIR == 0 and GPIO.input(sensorPIR) == 1):
                time.sleep(0.5)

                # simular que PIR esta detectando presença
                fixarPIR = 1
            if(fixarPIR == 1 and GPIO.input(sensorPIR) == 1):
                time.sleep(0.5)
                fixarPIR = 0
        
            print("...")
        
            # se porta 1 aberta então fechar
            if(P1==1):
                GPIO.output(porta1Fechando,1)
                print("1fechando")
            
            # fim de curso porta fechada
            if(GPIO.input(porta1Fechada) == 1):
                print("1fechada")
                GPIO.output(porta1Fechando,0)
                P1=0; # porta 1 fechada

            # enquanto brinco não lido ficar tentando ler
            if(not brincoLido):
                brinco=lerTag()
                
                matriz = matrizes.getMatrizByRfid(brinco)
                confinamento = confinamentos.getConfinamentoByMatriz(matriz['id'])
                
                quantidade = confinamentos.getQuantityForMatriz(matriz['id'])
                
                brincoLido=1    
                print ('Tag {}!'.format(brinco))

        if(fixarPIR == 0 ):

            brincoLido=0

            # se porta 1 fechada então abrir
            if(P1==0):
                GPIO.output(porta1Abrindo,1)
                print("1abrindo")

            # fim de curso porta fechada
            if(GPIO.input(porta1Aberta) == 1):
                GPIO.output(porta1Abrindo,0)
                print("1aberta")
                P1=1; # porta 1 aberta


if __name__ == "__main__":
    start()
