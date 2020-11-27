from flask import Flask
from root.root import root_bp
from api.api import api_bp

def initialize():
    app = Flask(__name__)
    app.register_blueprint(root_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app