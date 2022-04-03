from flask import render_template
from flask import Blueprint
from ...db import matrizCRUD

bp_atualizarMatriz = Blueprint("atualizarMatriz", __name__)

@bp_atualizarMatriz.route("/atualizarMatriz.html")
def atualizarMatriz():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
        }
    matrizes = matrizCRUD.consultarMatrizes()
    return render_template("main/atualizarMatriz.html", matrizes=matrizes, **templateData)