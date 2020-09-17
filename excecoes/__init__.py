class APIException(Exception):
    def __init__(self, status: int, mensagem: str):
        self.status_code = status
        self.mensagem = mensagem