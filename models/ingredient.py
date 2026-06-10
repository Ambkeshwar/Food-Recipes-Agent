from pydantic import BaseModel


class IngredientList(BaseModel):
    ingredients: list[str]