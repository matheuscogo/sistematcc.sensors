def init_app(app):
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projects/sistematcc.flask/src/sistemaTCC.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['CORS_HEADERS'] = "Content-Type"
    # app.config['CORS_RESOURCES'] = {r"/api/v1/*": {"origins": "http://192.168.0.105:3000/*"}}
    app.config['CORS_RESOURCES'] = {r"/api/v1/*": {"origins": "http://localhost:3000/*"}}
    # app.config['CORS_RESOURCES'] = {r"/api/v1/*": {"origins": "http://192.168.5.1:3000/*"}}
    app.config["CORS_ALLOW_HEADERS"] = "*"
    app.config["CORS_METHODS"] = ['GET', 'POST', 'DELETE', 'PUT', 'OPTIONS', 'HEAD']
    app.config['Access-Control-Allow-Origin'] = '*'