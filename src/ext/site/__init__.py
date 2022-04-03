from .view.index import bp_index
from .view.matrizes import bp_matrizes
from .view.registros import bp_registros
from .view.cadastrarMatriz import bp_cadastrarMatriz
from .controller.routes import bp_controller
from .view.atualizarMatriz import bp_atualizarMatriz
from .view.excluirMatriz import bp_excluirMatriz
from .view.login import bp_login
from .view.eventos import bp_eventos
from .view.cadastrarPlano import bp_cadastrarPlano
from .view.planos import bp_planos
from .view.detalhesMatriz import bp_detalhesMatriz
from .view.detalhesPlano import bp_detalhesPlano
from .view.cadastrarConfinamentro import bp_cadastrarConfinamento

def init_app(app):
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_matrizes)
    app.register_blueprint(bp_registros)
    app.register_blueprint(bp_cadastrarMatriz)
    app.register_blueprint(bp_controller)
    app.register_blueprint(bp_atualizarMatriz)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_excluirMatriz)
    app.register_blueprint(bp_eventos)
    app.register_blueprint(bp_cadastrarPlano)
    app.register_blueprint(bp_planos)
    app.register_blueprint(bp_detalhesMatriz)
    app.register_blueprint(bp_detalhesPlano)
    app.register_blueprint(bp_cadastrarConfinamento)