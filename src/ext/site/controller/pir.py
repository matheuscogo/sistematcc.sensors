from ext.config import sensors


def init_app(GPIO):
    GPIO.setup(sensors.sensorPIR, GPIO.IN)


def read(GPIO):
    return GPIO.input(sensors.sensorPIR) == 1


def motionSensor(hasMove):
    # TODO -> Sensor de movimento
    # Esperando movimento......
    # Detectou movimento, retornar TRUE
    # Tempo de espera
    # Bloco
    if hasMove:
        print("Matriz detectada pelo sensor de movimento")
    else:
        print("Não foi detectado nenhum movimento")
    # Bloco

    return hasMove
