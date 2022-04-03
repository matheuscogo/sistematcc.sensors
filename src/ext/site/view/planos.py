from flask import render_template
from flask import Blueprint
from ...db import planosCRUD

bp_planos = Blueprint("planos", __name__)

@bp_planos.route("/planos.html")
def planos():
    # try:
        templateData = {
            'title': 'Sistema de gerenciamento de matrizes',
        }
        planos = planosCRUD.consultarPlanos()
        return render_template("main/planos.html", planos=planos, **templateData)
    # except:
        # return render_template("main/matrizes.html", matrizes="erro", **templateData)
    # return render_template("main/matrizes.html", **templateData)
