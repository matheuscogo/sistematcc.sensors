from ast import Return
from weakref import ref

from sqlalchemy import true
import motor
import pir
import rfid
import time

def start():
    # Enquanto existir movimento no sensor
    while True:
        #Se movimento foi detectado, faça
        if options(1):
            # Fechar a porta de entrada -> porta(fechar)
            motor.porta()
            # Ler o RFID -> TEMPORIZADOR time(espere retorno em x tempo, funcao) -> retorno, animal valido ou sem RFID
            matriz = rfid.read()
            # Verifica se leu o RFID
            
            # Verificar se essa matriz pode ser separada -> motor.separador(abrir)
            motor.alimentador(matriz)  # Despejar a ração

        else:
            return False
            # Se o animal foi separado -> separador(fechar)
            # Não foi detectado nenhum movimento, abrir a porta de entrada -> porta(abrir)
            

def options(opc):
    # Opção 1 -> Sensor de movimento
    # Opção 2 -> Leitor RFID
    # Opção 3 -> Sensor de movimento
    # Opção 4 -> Sensor de movimento
    if opc == 1:
        print("Detectou movimento?")
        opc = input("1 - Sim\n2 - Não\n -> ")
        if opc == 1:
            print("Fechando a porta do alimentador....")
        elif opc == 2:
            print("Abrindo a porta do alimentador....")
            return False
        else:
            print("Opção inválida")
            options(1)
    elif opc == 2:
        print("Indentificou uma matriz?")
        opc = input("1 - Sim\n2 - Não\n -> ")
        if opc == 1:
            return True
        elif opc == 2:
            return False
        else:
            print("Opção inválida")
            options(2)
    else: 
        return False
    
            
            
if __name__ == "__main__":
    start()


# OBS:
    # VERIFICAR -> Fazer a verificação diaria dos alertas
    # VERIFICAR -> No leitor de RFID deverá existir um temporizador
