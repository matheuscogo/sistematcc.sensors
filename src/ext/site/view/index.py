from flask import render_template
from flask import Blueprint

bp_index = Blueprint("index", __name__)

@bp_index.route('/index')
@bp_index.route('/index.html')
@bp_index.route('/')
def index():
    templateData = {
        'title': 'Sistema de gerenciamento de matrizes',
        'color' : 'green'
    }
    return render_template("main/index.html", **templateData)