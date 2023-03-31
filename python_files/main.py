from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import crud
from jose import jwt
import hashlib
import sqlite3


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

# Fonctions utiles :
def hasher_mdp(mdp:str) -> str:
    return hashlib.sha256(mdp.encode()).hexdigest()

def decoder_token(token:str)->dict:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

def verifier_token(req: Request):
    token = req.headers["Authorization"] ## a modifier

# Classes contenu
class UserRegister(BaseModel):
    nom:str
    email:str
    mdp:str

class UserLogin(BaseModel):
    email:str
    mdp:str
    
class TransactionBuy(BaseModel):
    action_id: int

class TransactionSell(BaseModel):
    action_id: int
    prix_vente: float
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world "}

@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if crud.get_id_user_by_email(user.email) != None:
        raise HTTPException(status_code=403, detail="L'email fourni possède déjà un compte")
    else:
        id_user = crud.new_user(user.nom, user.email,  hasher_mdp(user.mdp), None)
        token = jwt.encode({
            "email" : user.email,
            "mdp" : user.mdp,
            "id" : id_user,
        }, SECRET_KEY, algorithm=ALGORITHM)
        crud.update_token(id_user, token)
        return {"token" : token}

@app.get("/api/mes-actions")
async def mes_actions(req: Request):
    try:
        decode = decoder_token(req.headers["Authorization"])
        id_user = crud.get_id_user_by_email(decode["email"])[0]
        action = crud.get_users_actions(id_user)
    except:
        raise HTTPException(status_code=401, detail="Vous devez être identifiés pour accéder à cet endpoint")
    return {"id_user": id_user, "action": action}

  
@app.post("/api/transaction/buy")
async def buy_transaction(transaction: TransactionBuy, req: Request):
    try:
        decode = decoder_token(req.headers["Authorization"])
        user_id = decode["id"]
        # Vérifier si l'action est disponible
        if not crud.is_action_available(transaction.action_id):
            return {"message": "Action not available."}

        # Acheter l'action
        crud.new_transaction_buying(user_id, transaction.action_id)
    except:
        raise HTTPException(status_code=401, detail="Vous devez être identifiés pour accéder à cet endpoint")
    return {"message": "Transaction added successfully."}


@app.post("/api/transaction/sell")
async def sell_transaction(transaction: TransactionSell, req: Request):
    try:
        decode = decoder_token(req.headers["Authorization"])
        user_id = decode["id"]
        action_available = crud.is_action_available(transaction.action_id)
        if  action_available:
            return {"message": "L'action n'est pas disponible à la vente"}
        else:
            crud.update_transaction_selling(user_id, transaction.action_id, transaction.prix_vente)
            crud.update_action_selling(transaction.action_id)
    except:
        raise HTTPException(status_code=401, detail="Vous devez être identifiés pour accéder à cet endpoint")
    return {"message": "La vente a été effectuée avec succès"}

@app.post("/api/follow")
async def follow_user(email: str, req: Request):
    try:
        decode = decoder_token(req.headers["Authorization"])
        following_user_id = crud.get_id_user_by_email(decode["email"])[0]
    except:
        raise HTTPException(status_code=401, detail="Vous devez être identifié pour accéder à cet endpoint")

    followed_users = crud.get_users_by_mail(email)
    if not followed_users:
        raise HTTPException(status_code=404, detail="L'utilisateur à suivre n'existe pas")

    followed_user_id = followed_users[0][0]
    if following_user_id == followed_user_id:
        raise HTTPException(status_code=400, detail="Vous ne pouvez pas vous suivre vous-même")

    if crud.is_following(following_user_id, followed_user_id):
        raise HTTPException(status_code=400, detail="Vous suivez déjà cet utilisateur")

    crud.user_follows(following_user_id, followed_user_id)

    return {"message": "Vous suivez maintenant l'utilisateur avec l'adresse e-mail {}".format(email)}


