import imp
from ..db import session
from ..site.model import Matriz
from ..site.model import Confinamento
from ..site.model import Dia
from ..site.model import Plano
from ..site.model import Registro
from ..site.model import Inseminacao
from ..site.model import Aviso


# def create_db():
#     """Creates database"""
#     db.create_all()
#     db.session.commit()


# def drop_db():
#     """Cleans database"""
#     db.drop_all()
#     db.session.commit()


def insert_plano():
    """Iserting plano"""
    plano = Plano(
        nome="Plano teste 01",
        descricao="Plano para testes 01",
        tipo=1,
        quantidadeDias=114,
        active=1
    )

    session.add(plano)
    session.commit()

    dias = '{"plano" : [{"dias": [1, 10],"quantidade": 1000},{"dias": [11, 21],"quantidade": 2000},{"dias": [22, 30],"quantidade": 2300},{"dias": [31, 40],"quantidade": 3000},{"dias": [41, 50],"quantidade": 4000},{"dias": [51, 100],"quantidade": 5000},{"dias": [101, 114],"quantidade": 6000}]}'

    planoObj = json.loads(str(dias))

    days = planoObj["plano"]

    for i in days:
        quantidade = i["quantidade"]
        dia1 = i["dias"][0]
        dia2 = i["dias"][1]
        for y in range(dia1, (dia2+1)):
            print("DIAS -> " + str(y))
            session.add(Dia(planoId=plano.id,
                            dia=y, quantidade=quantidade))
            session.commit()

        cadastrarPlano(plano)
