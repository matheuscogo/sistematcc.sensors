from flask import render_template, request
from flask import Blueprint
from ...db import planosCRUD
from ...db import matrizCRUD

bp_cadastrarConfinamento = Blueprint("cadastrarConfinamento", __name__)

@bp_cadastrarConfinamento.route('/cadastrarConfinamento.html', methods=['POST', 'GET'])
def cadastrarConfinamento():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
        'matriz' : request.args.get("id")
    }
    planos = planosCRUD.consultarPlanos()
    mtz = matrizCRUD.consultarMatriz(int(request.args.get("id")))
    print("------------------")
    print()
    #print("Matriz = " + str(request.args.get("id")) + " - " + str(type(int(request.args.get("id")))))
    print()
    print("------------------")
    return render_template("main/cadastrarConfinamento.html", planos=planos, mtz=mtz, **templateData)