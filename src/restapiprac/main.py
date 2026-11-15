from fastapi import FastAPI, APIRouter
from restapiprac.routers import items

app = FastAPI() 

app.include_router(items.router)