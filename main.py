from fasthtml.fastapp import *
from fastapi import FastAPI
from fastapi import  Request
#from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")
'''
accept html encoded as a block in parm=body
decode it and render it in the response
according to the css style included in the template
Input is html ( usually scraped from a page somewhere)
Output is minimally formatted text ( usually from a PW protected page)
'''
@app.get("/script")
async def read_item(request: Request, body: str = 'default'):
    
    return templates.TemplateResponse(
        request=request, name="athletic.html", context={"body": body})