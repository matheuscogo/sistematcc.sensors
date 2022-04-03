from ...db import registroCRUD
from flask import render_template, request
from flask import Blueprint
from ...db import planosCRUD
import json

bp_detalhesPlano = Blueprint("detalhesPlano", __name__)

@bp_detalhesPlano.route("/detalhesPlano.html", methods=['GET'])
def detalhesMatriz():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes'
    }
    plano = planosCRUD.consultarPlano(request.args.get("id"))
    dias = planosCRUD.consultarDia(request.args.get("id"))
    quantidade = planosCRUD.consultarQuantidade(request.args.get("id"))
#    dias = planosCRUD.consultarDias()
    return render_template("main/detalhesPlano.html", plano=plano, dias=dias, quantidade=quantidade, **templateData)