from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from src.extensions import db
from .models import User
from src.exceptions import ValidationError
from .exceptions import AuthError, UserAlreadyExistsError

class AuthService:
    @staticmethod
    def register(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise ValidationError("Username e senha são obrigatórios")

        if User.query.filter_by(username=username).first():
            raise UserAlreadyExistsError()

        new_user = User(
            username=username,
            password_hash=generate_password_hash(password)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user

    @staticmethod
    def login(data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise ValidationError("Username e senha são obrigatórios")

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password_hash, password):
            raise AuthError("Credenciais inválidas")

        access_token = create_access_token(identity=str(user.id))
        
        return {"access_token": access_token}


