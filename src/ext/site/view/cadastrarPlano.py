from flask import render_template
from flask import Blueprint

bp_cadastrarPlano = Blueprint("cadastrarPlano", __name__)

@bp_cadastrarPlano.route("/cadastrarPlano.html")
def cadastrarPlano():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes'
    }
    return render_template("main/cadastrarPlano.html", **templateData)