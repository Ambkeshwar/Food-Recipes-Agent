from agents.ingredient_agent import IngredientAgent
from agents.recipe_agent import RecipeAgent
from agents.ranking_agent import RankingAgent


class RecipeService:

    def __init__(self):

        self.ingredient_agent = IngredientAgent()
        self.recipe_agent = RecipeAgent()
        self.ranking_agent = RankingAgent()

    def process(self, image_path: str):

        ingredients = self.ingredient_agent.detect(
            image_path
        )

        recipes = self.recipe_agent.generate(
            ingredients["ingredients"]
        )

        ranked = self.ranking_agent.rank(
            ingredients["ingredients"],
            recipes
        )

        return ranked