from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Aqui apenas instanciamos as extensões.
# Elas serão iniciadas de verdade no __init__.py
db = SQLAlchemy()
jwt = JWTManager()
