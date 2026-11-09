from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/buy", response_class=HTMLResponse)
async def buy(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/rent", response_class=HTMLResponse)
async def rent(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )

@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )