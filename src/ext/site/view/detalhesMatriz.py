from ...db import registroCRUD
from flask import render_template, request
from flask import Blueprint
from ...db import registroCRUD, matrizCRUD

bp_detalhesMatriz = Blueprint("detalhesMatriz", __name__)

@bp_detalhesMatriz.route("/detalhesMatriz.html", methods=['GET'])
def detalhesMatriz():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes'
    }
    registros = registroCRUD.consultarRegistro(request.args.get("id"))
    matriz   = matrizCRUD.consultarMatriz(int(request.args.get("id")))
    return render_template("main/detalhesMatriz.html", registros=registros, matriz=matriz, **templateData)