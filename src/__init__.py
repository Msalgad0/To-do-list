from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from src.extensions import db, jwt
# Importamos o blueprint e a classe de erro
from src.modules.auth import auth_bp
from src.exceptions import APIError

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    jwt.init_app(app)

    # Handler de erros personalizado
    @app.errorhandler(APIError)
    def handle_api_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    # Handlers para erros de Token JWT
    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return jsonify({"error": True, "message": "Token expirado"}), 401

    @jwt.invalid_token_loader
    def invalid_token(error):
        return jsonify({"error": True, "message": "Token inválido"}), 401

    @jwt.unauthorized_loader
    def missing_token(error):
        return jsonify({"error": True, "message": "Token ausente"}), 401

    # Registra o módulo de Auth
    app.register_blueprint(auth_bp)

    # Importa os models para criar as tabelas
    from src.modules.auth.models import User
    from src.modules.todos.models import Todo

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return jsonify({"message": "API Rodando com Auth!"})

    return app
