from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (important for Chrome extension)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- CONFIG -----------
NOTION_TOKEN = "your_notion_token"
DATABASE_ID = "your_database_id"

class TextInput(BaseModel):
    text: str

# 🔗 Add task to Notion
def add_to_notion(task):
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": {
            "database_id": DATABASE_ID
        },
        "properties": {
            "Name": {   # ⚠️ MUST match your Notion column name
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

    # 🔍 DEBUG (very important)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)


# 🏠 Home route
@app.get("/")
def home():
    return {"message": "Notion AI Task Generator Running 🚀"}


# 🤖 Generate tasks
@app.post("/generate-tasks")
def generate_tasks(data: TextInput):
    idea = data.text

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