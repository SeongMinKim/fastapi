import os

from fastapi import FastAPI, File, UploadFile, Request, Form
from pydantic import BaseModel

from fastapi.templating import Jinja2Templates

# Run Script
from app.subprocess import look

app = FastAPI()


class Info(BaseModel):
    edge: str
    domain: str

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print(BASE_DIR)
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")


@app.get('/health')
async def health_check():
    return "OK"


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.post("/login")
def login(edge: str = Form(...), domain: str = Form(...)):
    return {"EDGE": edge, "DOMAIN": domain}


@app.get("/send-data")
async def send_data():
    print(look(edge="EDGETEST", domain="DOMAIN-TEST"))
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/migration", description="Posco Migration API")
async def migration(info: Info):
    diced_info = dict(info)
    return diced_info
