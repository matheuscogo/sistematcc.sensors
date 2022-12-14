from genericpath import exists
from queue import Empty

from responses import activate, delete

from ext.site.model.Inseminacao import Inseminacao
from ..site.model.Confinamento import Confinamento
from ..site.model import Registro
import datetime
from ..site.model.Dia import Dia
from ..site.model.Plano import Plano
from ..site.model.Aviso import Aviso
from ..site.model.Matriz import Matriz
from ..site.model.Registro import Registro
from sqlalchemy.sql import func
from datetime import datetime
from ext.db import session


def consultaConfinamentoPelaMatriz(matrizId):
    try:
        confinamento = session.query(Confinamento).filter_by(
            matrizId=matrizId, active=True, deleted=False).first()
        return confinamento
    except BaseException as e:
        return str(e)


def consultarQuantidadeAlimento(matrizId):
    try:
        confinamento = session.query(Confinamento).filter_by(
            matrizId=matrizId, active=True, deleted=False).first()

        dia = consultarQuantidadeDiasConfinamento(matrizId=confinamento.matrizId)
        
        dayQuantity = session.query(
            Dia.quantidade
        ).filter_by(
            planoId=confinamento.planoId, 
            dia=dia
        ).first()
        
        totalQuantity = session.query(func.sum(Registro.quantidade)).filter_by(
            confinamentoId=confinamento.id, dataEntrada=confinamento.dataConfinamento).first()[0]

        if totalQuantity is None:
            totalQuantity = 0

        total = dayQuantity[0] - totalQuantity

        if total <= 0:
            total = 0

        return total
    except BaseException as e:
        return e.args[0]


def canOpenDoor(matrizId):
    try:
        hasConfinamento = session.query(session.query(Confinamento).filter_by(matrizId=matrizId, active=True, deleted=False).exists()).scalar()
        if not hasConfinamento:
            return "Matriz não possui confinameto"
        
        hasInseminacao = session.query(session.query(Inseminacao).filter_by(matrizId=matrizId, active=True, deleted=False).exists()).scalar()
        if not hasInseminacao:
            return "Matriz não possui inseminação"

        confinamento = session.query(Confinamento).filter_by(matrizId=matrizId, active=True, deleted=False).first()
        
        hasWarning = session.query(session.query(Aviso).filter_by(confinamentoId=confinamento.id, active=True, deleted=False, tipo=2).exists()).scalar()
        if not hasWarning:
            return "Matriz não possui aviso de separação"
        
        canOpen = session.query(Aviso).filter_by(confinamentoId=confinamento.id, active=True, deleted=False).first()

        return canOpen.separate
    except BaseException as e:
        return e.args[0]


def consultarQuantidadeDiasConfinamento(matrizId):
    confinamento = session.query(Confinamento).filter_by(
        matrizId=matrizId, 
        active=True, 
        deleted=False
    ).first()

    day = (datetime.today() - confinamento.dataConfinamento).days

    if day == 0:
        day = 1
        
    return day
