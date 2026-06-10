# 🥗 Fridge Recipe Agent

An AI-powered recipe recommendation system that analyzes ingredients from a fridge image and generates personalized recipe suggestions.

The application uses:

* **Gemini 2.5 Flash** for ingredient detection from images
* **Groq Llama 3.1 8B Instant** for recipe generation and ranking
* **FastAPI** for API serving

---

## Architecture

```text
Image Upload
     │
     ▼
Gemini 2.5 Flash
(Ingredient Detection)
     │
     ▼
Structured Ingredients
     │
     ▼
Llama 3.1 8B Instant
(Recipe Generation)
     │
     ▼
Recipe Ranking
     │
     ▼
JSON Response
```

---

## Project Structure

```text
recipe-agent/
│
├── agents/
│   ├── ingredient_agent.py
│   ├── recipe_agent.py
│   └── ranking_agent.py
│
├── api/
│   └── recipe.py
│
├── core/
│   ├── config.py
│
├── models/
│
├── services/
│   └── recipe_service.py
│
├── utils/
│
├── images/
│   └── fridge.jpg
│
├── main.py
│
├── .env
│
├── requirements.txt
│
└── README.md
```

---

## Features

* Detect ingredients directly from fridge images
* Generate recipes based on available ingredients
* Rank recipes based on:

  * Ingredient match
  * Simplicity
  * Cooking time
  * Missing ingredients
* Fast API-based deployment
* Modular agent architecture

---

## Prerequisites

* Python 3.10+
* Gemini API Key
* Groq API Key

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd recipe-agent
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Requirements

```txt
fastapi
uvicorn
python-dotenv
langchain
langchain-groq
google-genai
pillow
python-multipart
pydantic
pydantic-settings
```

---

## Running the Application

Start FastAPI:

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Generate Recipes

**POST**

```http
/recipe
```

### Request

Form-data:

| Key  | Type |
| ---- | ---- |
| file | File |

Upload a fridge image.

---

### Example cURL

```bash
curl -X POST \
"http://127.0.0.1:8000/recipe" \
-F "file=@images/fridge.jpg"
```

---

## Sample Response

```json
{
  "ingredients": {
    "ingredients": [
      "tomato",
      "onion",
      "egg",
      "cheese"
    ]
  },
  "recipes": {
    "recipes": [
      {
        "title": "Cheese Omelette",
        "cook_time": "10 minutes",
        "difficulty": "Easy",
        "ingredients": [
          "egg",
          "cheese",
          "onion"
        ],
        "steps": [
          "Beat eggs",
          "Add cheese",
          "Cook in pan"
        ]
      }
    ]
  }
}
```

---

## Testing

### Local Test

Create:

```python
from services.recipe_service import RecipeService

service = RecipeService()

result = service.process(
    "images/fridge.jpg"
)

print(result)
```

Run:

```bash
python test_agent.py
```

---

## Workflow

### Ingredient Detection Agent

Uses Gemini Vision to:

* Analyze uploaded image
* Detect visible ingredients
* Return structured JSON

Example:

```json
{
  "ingredients": [
    "tomato",
    "onion",
    "egg"
  ]
}
```

### Recipe Generation Agent

Uses Groq Llama 3.1 8B to:

* Generate recipes
* Suggest cooking instructions
* Estimate cooking time
* Estimate difficulty

### Ranking Agent

Ranks recipes using:

* Ingredient utilization
* Ease of cooking
* Missing ingredient count
* Cooking duration

---

## Future Improvements

* Recipe database integration
* Nutritional information
* Calorie estimation
* User dietary preferences
* Vegetarian/Vegan filtering
* Recipe image generation
* Multi-language recipe support
* Redis caching
* Docker deployment
* Kubernetes deployment

---

## Troubleshooting

### JSONDecodeError

Gemini sometimes returns:

````text
```json
{
  "ingredients": []
}
````

````

Strip markdown before parsing.

---

### ModuleNotFoundError

Run from project root:

```bash
cd recipe-agent
uvicorn main:app --reload
````

Do not run modules from inside subfolders.

---

### Invalid API Key

Verify:

```env
GOOGLE_API_KEY=...
GROQ_API_KEY=...
```

and restart the application.

---

## Tech Stack

* FastAPI
* Gemini 2.5 Flash
* Groq Llama 3.1 8B Instant
* Python
* Pydantic
* LangChain

---

## License

MIT License
