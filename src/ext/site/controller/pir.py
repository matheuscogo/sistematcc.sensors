from ext.config import sensors
from ext.site.controller import motor
from ext.site.controller import button


def init_app(GPIO):
    GPIO.setup(sensors.sensorPIR, GPIO.IN)


def read(gpio):
    print("Aguardando detectção")
    readed = gpio.input(sensors.sensorPIR) == 1
    if readed:
        if button.closed(gpio) is False:
            motor.close(gpio)
            return True

    return False
