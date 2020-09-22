from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Para criação de endpoints com frontend
templates = Jinja2Templates(directory="full_api/templates")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
def index():
    return templates.get_template("index.html").render() 
