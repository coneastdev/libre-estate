from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

from sqlmodel import Field, SQLModel, create_engine, Session, select
import bcrypt
import jwt

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    password: str


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

def hashPassword(password: str) -> str:
    # converting password to array of bytes
    bytes = password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode()

def checkAccount(account: User) -> str:
    with Session(engine) as session:
        statement = select(User).where(User.email == account.email)
        results = session.exec(statement)
        for user in results:
            if (user.password == account.password):
                return "right-pass"
            else:
                print(user.password, account.password)
                return "wrong-pass"
    return "no-user"

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
async def login(request: Request, username: Annotated[str, Form()] = "", password: Annotated[str, Form()] = ""):
    print(username, password)
    return templates.TemplateResponse(
        request=request, name="login.html"
    )

@app.post("/login")
async def loginPost(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    hashedPass = hashPassword(password)
    account = User(email=email, password=hashedPass)

    if (checkAccount(account) == "right-pass"):
        return "true"
    else:
        return "false"

@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse(
        request=request, name="signup.html"
    )

@app.post("/signup")
async def signupPost(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    hashedPass = hashPassword(password)
    account = User(email=email, password=hashedPass)
    
    if (checkAccount(account) == "nouser"):
        with Session(engine) as session:

            session.add(account)

            session.commit()

    print(account)
    return f"{account}"