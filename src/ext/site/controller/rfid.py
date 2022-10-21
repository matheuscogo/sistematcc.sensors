from ...db import matrizCRUD
from ..controller import motor
import serial

ser = serial.Serial("/dev/serial0", 115200)
readDate = None


def init_app(GPIO):
    ...


def read(gpio):
    if ser.inWaiting() > 0:
        tag = ser.readline()
        tag = tag.decode("utf-8")  # bytes para str
        tag = tag.rstrip()

        matriz = matrizCRUD.consultarMatrizRFID(tag)
        if matriz is not None:
            if matriz.aviso.separar:
                motor.openSeparador(gpio)

            print('Matriz {} identificada'.format(matriz.rfid))
            return matriz

    return None


def readed(matriz):
    return matriz is not None
