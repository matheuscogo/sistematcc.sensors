# from .Aviso import Aviso
from .Confinamento import Confinamento
from .Dia import Dia
from .Inseminacao import Inseminacao
from .Matriz import Matriz
from .Plano import Plano
from .Registro import Registro


def init_app():
    # Aviso()
    Confinamento()
    Dia()
    Inseminacao()
    Matriz()
    Plano()
    Registro()
