from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Para criação de endpoints com frontend
templates = Jinja2Templates(directory="doc_sphinx/_build/html")


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
@router.get("/index.html", response_class=HTMLResponse, include_in_schema=False)
def index():
    return templates.get_template("index.html").render()
