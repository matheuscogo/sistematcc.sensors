from ext.config import sensors


def init_app(GPIO):
    GPIO.setup(sensors.cursoAbertura, GPIO.OUT)
    GPIO.setup(sensors.cursoFechamento, GPIO.OUT)
    GPIO.setup(sensors.cursoSepadorAbertura, GPIO.OUT)
    GPIO.setup(sensors.cursoSepadorFechamento, GPIO.OUT)


def opened(gpio):
    pressed = gpio.input(sensors.cursoAbertura) == 1
    if pressed:
        print("Portão aberto.")
        return pressed

    return False


def closed(gpio):
    pressed = gpio.input(sensors.cursoFechamento) == 1
    if pressed:
        print("Portão fechado.")
        return pressed

    return False
