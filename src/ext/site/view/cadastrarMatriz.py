from flask import render_template
from flask import Blueprint

bp_cadastrarMatriz = Blueprint("cadastrarMatriz", __name__)

@bp_cadastrarMatriz.route("/cadastrarMatriz.html")
def cadastrarMatriz():
    rfid = "teste"
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
        'rfid' : rfid
    }
    return render_template("main/cadastrarMatriz.html", **templateData)