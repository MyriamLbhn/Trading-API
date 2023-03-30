from fastapi import FastAPI, HTTPException, Request, Depends
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import crud
from jose import jwt
import hashlib

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
    est_entreprise:bool

class UserLogin(BaseModel):
    email:str
    mdp:str

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world "}

@app.post("/api/auth/inscription")
async def inscription(user:UserRegister):
    if crud.get_id_user_by_email(user.email) != None:
        raise HTTPException(status_code=403, detail="L'email fourni possède déjà un compte")
    else:
        id_user = crud.new_user(user.nom, user.email, user.est_entreprise, hasher_mdp(user.mdp), None)
        token = jwt.encode({
            "email" : user.email,
            "mdp" : user.mdp,
            "id" : id_user,
            "est_entreprise" : user.est_entreprise,
        }, SECRET_KEY, algorithm=ALGORITHM)
        crud.update_token(id_user, token)
        return {"token" : token}

# @app.get("/api/articles")
# async def mes_articles(req: Request):
#     try:
#         decode = decoder_token(req.headers["Authorization"])
#         id_user = crud.get_id_user_by_email(decode["email"])[0]
#         articles = crud.obtenir_article_user(id_user)
#         return {"id_user": id_user, "articles": articles}
#     except:
#         raise HTTPException(status_code=401, detail="Vous devez être identifiés pour accéder à cet endpoint")