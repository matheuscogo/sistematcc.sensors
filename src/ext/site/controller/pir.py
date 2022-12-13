from ext.config import sensors
from ext.site.controller import motor
from ext.site.controller import button


def init_app(GPIO):
    GPIO.setup(sensors.sensorPIR, GPIO.IN)


def read(gpio):
    print("Aguardando detectção")
    readed = gpio.input(sensors.sensorPIR) == 1
    if readed:
        if button.opened(gpio):
            motor.close(gpio)
            return True

        if button.closed(gpio):
            return True

    return False
