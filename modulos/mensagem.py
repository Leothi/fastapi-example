from fastapi.responses import JSONResponse

def mensagem_upper(string: str) -> str:
    if string:
        return string.upper()
    else:
        return JSONResponse(status_code=400, content={"message": "Item not found"})
