import os
import tempfile

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.recipe_service import RecipeService

router = APIRouter()

service = RecipeService()


@router.post("/recipe")
async def generate_recipe(
    file: UploadFile = File(...)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        tmp.write(await file.read())
        path = tmp.name

    try:
        return service.process(path)

    finally:
        os.remove(path)