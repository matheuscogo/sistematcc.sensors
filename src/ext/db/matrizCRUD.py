from ext.site.model import Matriz
from ext.site.model import Confinamento
from ext.db import session
from ext.db import confinamentoCRUD
from datetime import datetime
import uuid


def consultarMatrizRFID(rfid):  # Read
    try:
        matriz = session.query(Matriz).filter_by(
            rfid=rfid,
            deleted=False
        ).first()

        if matriz is None:
            return None

        matriz.entrada = datetime.now()
        matriz.hash = str(uuid.uuid4())
        matriz.quantidadeTotal = confinamentoCRUD.consultarQuantidadeAlimento(
            matriz.id)
        matriz.separate = confinamentoCRUD.canOpenDoor(matriz.id)
        matriz.confinamentoId = session.query(Confinamento).filter_by(
            matrizId=matriz.id, active=True).first()

        return matriz
    except Exception as e:
        return e.args[0]
