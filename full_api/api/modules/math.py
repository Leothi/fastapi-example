from loguru import logger

from api.exceptions.math import DivisaoPorZeroException


def dobro(valor: float) -> float:
    """Retorna o valor de entrada.

    :param valor: Valor para ser dobrado.
    :type valor: float
    :return: Valor dobrado.
    :rtype: float
    """
    logger.info("Calculando dobro do valor de entrada")
    return valor * 2


def divisao(numerador: float, denominador: float) -> float:
    """Retorna o resultado da divisão.

    :param numerador: Numerador da fração.
    :type numerador: float
    :param denominador: Denominador da fração.
    :type denominador: float
    :return: Resultado da operação.
    :rtype: float
    """
    logger.info("Calculando a divisão dos valores de entrada")
    if denominador == 0:
        raise DivisaoPorZeroException
    return numerador / denominador
