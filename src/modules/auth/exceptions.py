from src.exceptions import APIError

class AuthError(APIError):
    def __init__(self, message="Falha na autenticação"):
        super().__init__(message, status_code=401)

class UserAlreadyExistsError(APIError):
    def __init__(self, message="Este usuário já existe"):
        super().__init__(message, status_code=409)
