#!/usr/bin/env python3.7
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
from pirc522 import RFID
import time

led1=40

bot1=37
bot2=35
led2=38
led3=36

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte
GPIO.setup(bot1,GPIO.IN)
GPIO.setup(bot2,GPIO.IN)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
rc522 = RFID() #On instancie la lib

RFID_ID_CATAO = [219, 154, 79, 67, 77]
RFID_ID_TAG = [116, 95, 92, 211, 164]

print('Aproxime a Tag (Ou saia com Ctrl + c): ')

#On va faire une boucle infinie pour lire en boucle
while True :

    if(GPIO.input(bot1) == 1):
        GPIO.output(led1,1)
        time.sleep(0.5)
        GPIO.output(led1,0)

    rc522.wait_for_tag() #On attnd qu'une puce RFID passe à portée
    (error, tag_type) = rc522.request() #Quand une puce a été lue, on récupère ses infos

    if not error : #Si on a pas d'erreur
        (error, uid) = rc522.anticoll() #On nettoie les possibles collisions, ça arrive si plusieurs cartes passent en même temps

        if not error : #Si on a réussi à nettoyer
            #print('A tag')
            #print('A tag é: {}'.format(uid)) #On affiche l'identifiant unique du badge RFID
            if RFID_ID_CATAO == uid :
                print('Cartão {} autenticado !'.format(uid))
            else :
                if RFID_ID_TAG == uid :
                    print('Tag {} autenticada !'.format(uid))
                else :
                    print('NÃO IDENTIFICADO')
            time.sleep(1) #On attend 1 seconde