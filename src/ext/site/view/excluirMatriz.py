from flask import render_template
from flask import Blueprint
from ...db import matrizCRUD

bp_excluirMatriz = Blueprint("excluirMatriz", __name__)

@bp_excluirMatriz.route("/excluirMatriz.html")
def excluirMatriz():
    try:
        templateData = {
            'title': 'Sistema de gerenciamento de matrizes',
        }
        matrizes = matrizCRUD.consultarMatrizes()
        return render_template("main/excluirMatriz.html", matrizes=matrizes, **templateData)
    except:
        return render_template("main/excluirMatriz.html", matrizes="erro", **templateData)