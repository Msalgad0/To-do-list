class APIError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = True
        rv['message'] = self.message
        return rv

class ValidationError(APIError):
    def __init__(self, message="Dados de entrada inválidos"):
        super().__init__(message, status_code=400)

class ServerError(APIError):
    def __init__(self, message="Erro interno no servidor"):
        super().__init__(message, status_code=500)

