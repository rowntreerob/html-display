from fasthtml.fastapp import *
from fastapi import FastAPI
from fastapi import  Request
#from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

@app.get("/script")
async def read_item(request: Request, body: str = 'default'):
    return templates.TemplateResponse(
        request=request, name="athletic.html", context={"body": body})