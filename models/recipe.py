from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    cook_time: str
    difficulty: str
    ingredients: list[str]
    instructions: list[str]


class RecipeResponse(BaseModel):
    recipes: list[Recipe]