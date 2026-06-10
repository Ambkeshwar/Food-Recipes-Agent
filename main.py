from fastapi import FastAPI

from api.recipe import router

app = FastAPI(
    title="Fridge Recipe Agent"
)

app.include_router(router)