# 🚀 Notion AI Task Generator — Complete Final Submission

## 🏆 Hackathon Submission

### 📌 Description
I built an AI-powered productivity system that converts ideas into structured tasks and automatically syncs them into Notion using a Chrome extension and FastAPI backend. This system eliminates manual planning and integrates workflows across tools, creating a seamless execution pipeline.

---

## 🌟 Features
- ✨ Convert ideas into actionable tasks  
- 🧠 AI-style task breakdown  
- 🔗 Automatic sync with Notion database  
- 🌐 Cloud backend (GitHub Codespaces)  
- 🧩 Chrome extension interface  
- ⚡ Real-time task generation  

---

## 📦 Project Structure

```text
chrome-ai-extension/
├── backend/
│   └── main.py            # FastAPI server & Notion API logic
├── extension/
│   ├── manifest.json      # Extension configuration (V3)
│   ├── popup.html         # Extension UI
│   ├── popup.js           # Frontend logic & API calls
│   └── style.css          # Extension styling
└── README.md              # Project documentation


---

## 🛠️ Tech Stack
- Frontend: JavaScript, HTML, CSS  
- Backend: FastAPI (Python)  
- API Integration: Notion API  
- Deployment: GitHub Codespaces  

---

## 📦 Project Structure

chrome-ai-extension/
│── main.py
│── manifest.json
│── popup.html
│── popup.js
│── style.css
│── README.md


---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone https://github.com/your-username/chrome-ai-extension.git

cd chrome-ai-extension


### 2. Install Dependencies

pip install fastapi uvicorn requests


### 3. Configure Notion API
- Go to: https://www.notion.so/my-integrations  
- Create a new integration  
- Copy the Internal Integration Secret  

Update in `main.py`:

NOTION_TOKEN = "your_secret_token"
DATABASE_ID = "your_database_id"


---

### 4. Setup Notion Database
- Create a Table (Full Page)  
- Rename first column to:

Name

- Click `••• → Connections → Add AI Task Generator`

---

### 5. Run Backend

python3 -m uvicorn main:app --reload


---

### 6. Load Chrome Extension
- Open chrome://extensions/  
- Enable Developer Mode  
- Click Load Unpacked  
- Select project folder  

---

### 7. Update API URL
In `popup.js`:

fetch("https://your-codespace-url/generate-tasks
", {


---

## 🚀 Usage
1. Open Chrome Extension  
2. Enter idea  
3. Click Generate Tasks  
4. Tasks automatically appear in Notion  

---

## 🎬 Demo Flow
1. Open Chrome Extension  
2. Enter idea  
3. Click Generate  
4. Open Notion  
5. Tasks appear automatically  

---

## 🧠 Example

### Input

Build AI Chrome Extension


### Output
- 🔍 Research requirements  
- 🧠 Design architecture  
- 💻 Develop core features  
- 🧪 Test and debug  
- 🚀 Deploy project  

---

## ⚡ Highlights
- Eliminates manual planning  
- Centralizes workflow in Notion  
- Demonstrates AI + automation  
- Full-stack cloud-based system  

---

## 🧠 Debugging Lessons

### Tasks not appearing

Fix: Column name must be "Name"


### Integration not working

Fix: Use ••• → Connections (not Invite)


### Extension not working

Fix: Use Codespaces public URL instead of localhost


---

## 🏁 Final Status

| Component            | Status |
|---------------------|--------|
| FastAPI Backend     | ✅     |
| Chrome Extension    | ✅     |
| Notion Integration  | ✅     |
| Cloud Deployment    | ✅     |
| End-to-End System   | ✅     |

---

## 🔥 Final Result

Beginner → Full Stack Builder 🚀


---

## 🔮 Future Improvements
- Add OpenAI / Groq API  
- GitHub issue automation  
- Smart prioritization  
- AI agent workflows  

---

## 👨‍💻 Author
Durga Dhanush Yaragani
