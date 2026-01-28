from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from src.extensions import db, jwt

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuração do Banco de Dados (Pega do .env)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Inicializa as extensões com a app configurada
    db.init_app(app)
    jwt.init_app(app)

    # Rota de teste simples (só para ver se funciona)
    @app.route('/')
    def index():
        return jsonify({"message": "API Rodando e Conectada com Sucesso!"})

    return app

