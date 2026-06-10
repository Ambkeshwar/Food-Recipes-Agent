from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
import re


class RankingAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

    def rank(self, ingredients, recipes):

        prompt = ChatPromptTemplate.from_template(
            """
            You are a recipe ranking expert.
            Do not use markdown.
            Do not use ```json.

            Rank recipes based on:

            1. Ingredient match percentage
            2. Simplicity
            3. Fewest missing ingredients
            4. Fastest cooking time

            Return ONLY valid JSON.

            {{
                "ranked_recipes":[
                    {{
                        "rank":1,
                        "title":"",
                        "score":0,
                        "reason":""
                    }}
                ]
            }}

            Ingredients:
            {ingredients}

            Recipes:
            {recipes}
            """
        )

        chain = prompt | self.llm

        response = chain.invoke(
            {
                "ingredients": ingredients,
                "recipes": json.dumps(recipes, indent=2)
            }
        )

        content = response.content.strip()

        # Remove markdown if model returns ```json
        content = re.sub(r"^```json", "", content)
        content = re.sub(r"^```", "", content)
        content = re.sub(r"```$", "", content)

        return json.loads(content.strip())