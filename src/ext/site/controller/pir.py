from ext.config import sensors
from ext.site.controller import motor
from ext.site.controller import button


def init_app(GPIO):
    GPIO.setup(sensors.sensorPIR, GPIO.IN)


def read(gpio):
    if gpio.input(sensors.sensorPIR) == 1:
        if button.opened(gpio):
            motor.close(gpio)
            return True

        if button.closed(gpio):
            return True

    return False


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
