from flask import Blueprint
from flask_restx import Api, resource
from flask_cors import CORS

from .routes import matrizes, planos, registros, confinamento, dias, inseminacao

cors = CORS()

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Api(
    Blueprint('API - Vult Scire', __name__),
    title='API para gestão do sistema de alimentação de matrizes de suinas',
    version='1.0',
    description='Endpoints para criação, consulta, alteração e exclusão para cosumo.',
    authorizations=authorizations, 
    security='apikey',
)

registros.bind_with_api(api)

def init_app(app):
    app.register_blueprint(api.blueprint, url_prefix='/api/v1')
    cors.init_app(app)