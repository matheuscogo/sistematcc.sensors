from flask import render_template
from flask import Blueprint

bp_login = Blueprint("login", __name__)

@bp_login.route('/login')
def login():
    templateData = {
        
    }
    return render_template("auth/login.html", **templateData)