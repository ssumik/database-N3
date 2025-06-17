# To run the application in dev mode, use'fastapi dev main.py'
from fastapi import FastAPI

from api.controllers.clients import router as clients_router
from api.database.database import DataBase
from api.models.client import Client

app = FastAPI()

@app.on_event("startup")
async def startup():
    database = DataBase()
    database.MODELS = [
        Client
    ]
    await database.init()
    
    # Add the routes to application
    app.include_router(clients_router)