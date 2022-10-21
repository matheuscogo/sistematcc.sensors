from ...db import matrizCRUD
import serial

ser = serial.Serial("/dev/serial0", 115200)
readDate = None


def init_app(GPIO):
    ...


def read():
    if ser.inWaiting() > 0:
        tag = ser.readline()
        tag = tag.decode("utf-8")  # bytes para str
        tag = tag.rstrip()

        matriz = matrizCRUD.consultarMatrizRFID(tag)
        if matriz is not None:
            print('Matriz {} identificada'.format(matriz.rfid))
            return matriz

    return None


def readed(matriz):
    return matriz is not None
