from api.exceptions import APIException


class DivisaoPorZeroException(APIException):
    def __init__(self):
        mensagem = "O denominador não pode ser 0."
        super().__init__(400, mensagem)
