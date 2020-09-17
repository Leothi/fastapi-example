from fastapi.responses import JSONResponse

def mensagem_upper(string: str) -> str:
    """Transforma a mensagem para upper case.

    :param string: string de entrada.
    :type string: str
    :return: string em upper case.
    :rtype: str
    """    
    if string:
        return string.upper()
    else:
        return JSONResponse(status_code=400, content={"message": "Item not found"})
