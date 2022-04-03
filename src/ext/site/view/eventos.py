from flask import render_template
from flask import Blueprint

bp_eventos = Blueprint("eventos", __name__)

@bp_eventos.route('/eventos')
def eventos():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
        'color' : 'green'
    }
    return render_template("main/eventos.html", **templateData)