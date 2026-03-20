from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# ----------- CONFIG -----------
NOTION_TOKEN = "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"
DATABASE_ID = "32930fd6f0e080158638f04c9d4ae2c1"

# ----------- MODEL -----------
class TextInput(BaseModel):
    text: str

# ----------- NOTION FUNCTION -----------
def add_to_notion(task):
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": task
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response.status_code

# ----------- ROUTES -----------

@app.get("/")
def home():
    return {"message": "Notion AI Task Generator Running 🚀"}

@app.post("/generate-tasks")
def generate_tasks(data: TextInput):
    idea = data.text

    # Fake AI (fast & reliable for hackathon)
    tasks = [
        f"🔍 Research requirements for {idea}",
        f"🧠 Design architecture for {idea}",
        f"💻 Develop core features",
        f"🧪 Test and debug",
        f"🚀 Deploy project"
    ]

    for task in tasks:
        add_to_notion(task)

    return {
        "message": "Tasks added to Notion ✅",
        "tasks": tasks
    }
