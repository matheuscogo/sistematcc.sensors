#!/usr/bin/env python3.7
# -- coding: utf-8 --

import RPi.GPIO as GPIO  # Importe la bibliothèque pour contrôler les GPIOs

import time

leitor = 5
porta1Fechada = 6
porta1Aberta = 13
porta2Fechada = 19
porta2Aberta = 26

led1 = 0
led2 = 0

porta1Fechando = 12
porta1Abrindo = 16
porta2Fechando = 20
porta2Abrindo = 21

GPIO.setmode(GPIO.BOARD)  # Définit le mode de numérotation (Board)
GPIO.setwarnings(False)  # On désactive les messages d'alerte
GPIO.setup(leitor, GPIO.IN)
GPIO.setup(porta1Fechada, GPIO.IN)
GPIO.setup(porta2Fechada, GPIO.IN)
GPIO.setup(porta1Aberta, GPIO.IN)
GPIO.setup(porta2Aberta, GPIO.IN)
GPIO.setup(porta1Fechando, GPIO.OUT)
GPIO.setup(porta1Abrindo, GPIO.OUT)
GPIO.setup(porta2Fechando, GPIO.OUT)
GPIO.setup(porta2Abrindo, GPIO.OUT)

RFID_ID_CATAO = [219, 154, 79, 67, 77]
RFID_ID_TAG = [116, 95, 92, 211, 164]


def lerTag():
    tag = ["123456789", "987654321"]
    return 'hello world'


print('Aproxime a Tag (Ou saia com Ctrl + c): ')

uid = ''
# On va faire une boucle infinie pour lire en boucle
while True:

    if(GPIO.input(leitor) == 1):
        GPIO.output(led1, 1)
        time.sleep(0.5)
        GPIO.output(led1, 0)

        # print('A tag é: {}'.format(uid)) #On affiche l'identifiant unique du badge RFID
        if RFID_ID_CATAO == uid:
            print('Cartão {} autenticado !'.format(uid))
        else:
            if RFID_ID_TAG == uid:
                print('Tag {} autenticada !'.format(uid))
            else:
                print('NÃO IDENTIFICADO')
        time.sleep(1)  # On attend 1 seconde
