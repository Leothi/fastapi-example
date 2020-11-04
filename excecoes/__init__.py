class APIException(Exception):
    """Classe base para criação de Exceções personalizadas da API.

    :param Exception: Classe Python de Exceções.
    """

    def __init__(self, status: int, mensagem: str):
        self.status_code = status
        self.mensagem = mensagem
