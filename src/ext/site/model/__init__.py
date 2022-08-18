from ext.site.model.Aviso import Aviso
from ext.site.model.Confinamento import Confinamento
from ext.site.model.Dia import Dia
from ext.site.model.Inseminacao import Inseminacao
from ext.site.model.Matriz import Matriz
from ext.site.model.Plano import Plano
from ext.site.model.Registro import Registro
from ext.site.model.Alimentador import Alimentador


def init_app():
    Aviso()
    Confinamento()
    Dia()
    Inseminacao()
    Matriz()
    Plano()
    Registro()
    Alimentador()
