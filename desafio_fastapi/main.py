from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
from typing import List, Optional
import jwt
import datetime

app = FastAPI(
    title="API Bancária Assíncrona",
    description="API para gerenciar operações bancárias de depósitos e saques",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    username: str
    password: str

class Account(BaseModel):
    id: int
    balance: float

class Transaction(BaseModel):
    id: int
    account_id: int
    amount: float
    type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        user_id: int = payload.get("user_id")
        username: str = payload.get("username")
        return User(username=username, password="")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

@app.post("/token")
async def login_for_access_token(form_data: OAuth2):
    user_dict = {"username": form_data.username, "password": form_data.password}
    user = User(**user_dict)
    if user.username == "admin" and user.password == "admin":
        user_id = 1
        expires_in = datetime.timedelta(minutes=30)
        access_token_expires = datetime.datetime.utcnow() + expires_in
        access_token = jwt.encode(
            {"user_id": user_id, "username": user.username, "exp": access_token_expires},
            "secret",
            algorithm="HS256",
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/accounts/")
async def read_accounts(current_user: User = Depends(get_current_user)):
    accounts = [
        Account(id=1, balance=1000.0),
        Account(id=2, balance=500.0),
    ]
    return accounts

@app.get("/accounts/{account_id}")
async def read_account(account_id: int, current_user: User = Depends(get_current_user)):
    account = Account(id=account_id, balance=1000.0)
    return account

@app.post("/transactions/")
async def create_transaction(transaction: Transaction, current_user: User = Depends(get_current_user)):
    if transaction.amount < 0:
        raise HTTPException(status_code=400, detail="Valor de transação inválido")
    account = Account(id=transaction.account_id, balance=1000.0)
    if transaction.type == "deposit":
        account.balance += transaction.amount
    elif transaction.type == "withdrawal":
        if account.balance < transaction.amount:
            raise HTTPException(status_code=400, detail="Saldo insuficiente")
        account.balance -= transaction.amount
    return transaction

@app.get("/transactions/{account_id}")
async def read_transactions(account_id: int, current_user: User = Depends(get_current_user)):
    transactions = [
        Transaction(id=1, account_id=account_id, amount=100.0, type="deposit"),
        Transaction(id=2, account_id=account_id, amount=50.0, type="withdrawal"),
    ]
    return transactions

@app.get("/docs", response_class=HTMLResponse)
async def get_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Bancária Assíncrona")

@app.get("/openapi.json", response_class=JSONResponse)
async def openapi():
    return JSONResponse(content=get_openapi(title="API Bancária Assíncrona", version="1.0.0", routes=app.routes), media_type="application/json")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)