import RPi.GPIO as GPIO
from pirc522 import RFID
from datetime import datetime
import time

from os import sys
sys.path.append("..")

import Registro
from ...db import matrizCRUD, registroCRUD, confinamentoCRUD

import sys
sys.path.insert(1, '../model')
sys.path.insert(2, '../view')
sys.path.insert(3, '../controller')

bot1 = 37
bot2 = 35
led1 = 40
led2 = 38
led3 = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(bot1, GPIO.IN)
GPIO.setup(bot2, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
rc522 = RFID()


while True:
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()

    if not error:
        (error, uid) = rc522.anticoll()
    if not error:
        entrada = 1
        while entrada:
            if not matrizCRUD.existsRFID(str(uid)):
                registro = Registro()
                print('Matriz {} identificada'.format(uid))
                registro(dataEntrada=str(datetime.now().strftime("%d/%m/%Y")))
                registro(horaEntrada=str(datetime.now().strftime("%H:%M:%S")))
                registro(matriz=matrizCRUD.consultarMatrizID(str(uid)))
                GPIO.output(led1, 1)
                time.sleep(1)
                GPIO.output(led1, 0)
                numero = 0
                alimentador = 1;
                while alimentador:
                    if (GPIO.input(bot1) == 1):
                        print('Matriz {} solicitou alimento'.format(uid))
                        numero = numero + 1
                        GPIO.output(led3, 1)
                        time.sleep(1)
                        GPIO.output(led3, 0)
                        alimentador = 1
                    if (GPIO.input(bot2) == 1):
                        GPIO.output(led2, 1)
                        time.sleep(1)
                        GPIO.output(led2, 0)
                        registro(dataSaida=str(datetime.now().strftime("%d/%m/%Y")))
                        registro(horaSaida=str(datetime.now().strftime("%H:%M:%S")))
                        registroCRUD.cadastrarRegistro(registro)
                        print('Matriz {} saiu do alimentador'.format(uid))
                        print('Reiniciando sistema')
                        alimentador = 0
                        entrada = 0
            else:
                print("erro rfid")