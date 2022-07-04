import schedule
import time


def init_app():
    if datetime.datetime.today().hour - horaVeficada > 24:
        confinamentos.verifyDaysToOpen()
        horaVeficada = datetime.datetime.today().hour
