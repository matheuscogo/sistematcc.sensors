from ...db import matrizCRUD
from ..controller import motor
import serial
ser = serial.Serial("/dev/serial0", 115200)


def init_app(GPIO):
    ...


def read(gpio):
    print("Aguardando identificação")
    if ser.inWaiting() > 0:
        tag = ser.readline()
        tag = tag.decode("utf-8")
        tag = tag.rstrip()

    matriz = matrizCRUD.consultarMatrizRFID(tag)

    if matriz is not None:
        if matriz.separate:
            motor.openSeparador(gpio)

        print('Matriz {} identificada'.format(matriz.rfid))
        return matriz
