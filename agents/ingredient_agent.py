from google import genai
from PIL import Image
from dotenv import load_dotenv
import os
import json

load_dotenv()

class IngredientAgent:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

    def detect(self, image_path):

        image = Image.open(image_path)

        prompt = """
        Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not provide explanations.

Format:

{
  "ingredients": [
    "tomato",
    "onion"
  ]
}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, image]
        )

        return json.loads(response.text)