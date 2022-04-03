from flask import render_template
from flask import Blueprint
from ...db import matrizCRUD

bp_matrizes = Blueprint("matrizes", __name__)

@bp_matrizes.route("/matrizes.html")
def matrizes():
    try:
        templateData = {
            'title': "Sistema de gerenciamento de matrizes",
        }
        matrizes = matrizCRUD.consultarMatrizes()
        return render_template("main/matrizes.html", matrizes=matrizes, **templateData)
    except:
        return render_template("main/matrizes.html", **templateData)