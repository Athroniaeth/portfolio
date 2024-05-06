from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.staticfiles import StaticFiles

from portfolio import STATIC_PATH
from portfolio.router import router

# Crée l'application FastAPI
app = FastAPI()

# Ajoutes les routes
app.include_router(router)

# Ajoutes les fichiers statiques aux routes
app.mount('/static', StaticFiles(directory=STATIC_PATH), name="static")

# Rend l'application compatible avec AWS Lambda / API Gateway (seulement en production)
# handler = Mangum(app)
