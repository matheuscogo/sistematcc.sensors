from ext.config import sensors


def init_app(GPIO):
    GPIO.setup(sensors.cursoAbertura, GPIO.OUT)
    GPIO.setup(sensors.cursoFechamento, GPIO.OUT)
    GPIO.setup(sensors.cursoSepadorAbertura, GPIO.OUT)
    GPIO.setup(sensors.cursoSepadorFechamento, GPIO.OUT)


def opened(gpio):
    return gpio.input(sensors.cursoAbertura) == 1


def closed(gpio):
    return gpio.input(sensors.cursoFechamento) == 1


def separadorOpened(gpio):
    pressed = gpio.input(sensors.cursoSepadorAbertura) == 1
    if pressed:
        print("Portão aberto.")
        return pressed

    return False


def separadorClosed(gpio):
    pressed = gpio.input(sensors.cursoSepadorFechamento) == 1
    if pressed:
        print("Portão fechado.")
        return pressed

    return False
