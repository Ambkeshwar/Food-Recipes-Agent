from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json


class RecipeAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.1-8b-instant"
        )

    def generate(self, ingredients):

        prompt = ChatPromptTemplate.from_template(
            """
            Available ingredients:

            {ingredients}

            Generate 5 recipes.

            Return JSON only.

            {{
                "recipes":[
                    {{
                        "title":"",
                        "cook_time":"",
                        "difficulty":"",
                        "ingredients":[],
                        "steps":[]
                    }}
                ]
            }}
            """
        )

        chain = prompt | self.llm

        result = chain.invoke(
            {
                "ingredients": ingredients
            }
        )

        content = result.content

        start = content.find("{")
        end = content.rfind("}") + 1

        return json.loads(
            content[start:end]
        )