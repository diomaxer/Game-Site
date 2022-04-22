from fastapi import FastAPI
from routers import games_router


app = FastAPI()

app.include_router(router=games_router.router, prefix="/v1/games", tags=["games"])