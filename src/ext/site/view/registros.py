from flask import render_template, request
from flask import Blueprint
from ...db import registroCRUD

bp_registros = Blueprint("registros", __name__)

@bp_registros.route("/registros.html")
def registros():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
    }
    registros = registroCRUD.consultarRegistros()
    return render_template("main/registros.html", registros=registros, **templateData)