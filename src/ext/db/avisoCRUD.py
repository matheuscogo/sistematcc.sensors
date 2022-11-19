from ..site.model.Aviso import Aviso
from ..db import db
import datetime
from werkzeug.wrappers import Response, Request
from xmlrpc.client import ResponseError
import json
from ..db import db
from datetime import datetime


def cadastrarAviso(confinamentoId, type):  # Create
    try:
        dataAviso = datetime.today
        
        db.session.add(
            Aviso(
                confinamentoId=confinamentoId,
                dataAviso=dataAviso,
                type=type,
                separate=False,
                active=True,
                deleted=False
            )
        )
        db.session.commit()
        return True
    except BaseException as e:
        return False