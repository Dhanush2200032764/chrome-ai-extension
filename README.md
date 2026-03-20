# 🚀 Notion AI Task Generator — Complete Final Submission

## 🏆 Hackathon Submission

### 📌 Description
I built an AI-powered productivity system that converts raw ideas into structured tasks and automatically syncs them into Notion using a Chrome extension and a FastAPI backend. This system eliminates manual planning and integrates workflows across tools, creating a seamless execution pipeline.

### 🌟 Features
* **✨ Idea Transformation:** Convert vague thoughts into actionable steps.
* **🧠 AI-Style Logic:** Automated task breakdown for project management.
* **🔗 Notion Sync:** Real-time database updates via official Notion API.
* **🌐 Cloud Powered:** Backend hosted via GitHub Codespaces for 24/7 accessibility.
* **🧩 Minimalist UI:** Lightweight Chrome extension for instant access.

---

## 🛠️ Tech Stack
* **Frontend:** JavaScript (ES6+), HTML5, CSS3
* **Backend:** FastAPI (Python)
* **API Integration:** Notion REST API
* **Deployment:** GitHub Codespaces / Uvicorn

---

## 📦 Project Structure
```text
chrome-ai-extension/
├── main.py            # FastAPI server & Notion API logic
├── manifest.json      # Extension configuration (Manifest V3)
├── popup.html         # Extension UI elements
├── popup.js           # Frontend logic & API fetch calls
├── style.css          # Extension styling & layout
└── README.md          # Project documentation
⚙️ Setup Instructions1. Clone & PrepareBashgit clone [https://github.com/YARAGANIDURGADHANUSH/chrome-ai-extension.git](https://github.com/YARAGANIDURGADHANUSH/chrome-ai-extension.git)
cd chrome-ai-extension
pip install fastapi uvicorn requests
2. Configure Notion APIGo to: Notion IntegrationsCreate a new integration and copy the Internal Integration Secret.Update the following variables in main.py:NOTION_TOKEN = "your_secret_token"DATABASE_ID = "your_database_id"3. Setup Notion DatabaseCreate a Table (Full Page).Rename the first column to exactly: Name.Click ••• (Top Right) → Connections → Add AI Task Generator.4. Launch BackendBashpython3 -m uvicorn main:app --reload
5. Install Chrome ExtensionOpen chrome://extensions/.Enable Developer Mode.Click Load Unpacked and select the project folder.Important: Update the API URL in popup.js to your public Codespaces URL.🚀 Usage & Demo FlowOpen the Chrome Extension from your browser bar.Enter an idea (e.g., "Build a portfolio website").Click Generate Tasks.Switch to Notion — tasks appear automatically with status and icons.🧠 Example OutputInput: Build AI Chrome ExtensionOutput:🔍 Research requirements🧠 Design architecture💻 Develop core features🧪 Test and debug🚀 Deploy project🏁 Final StatusComponentStatusFastAPI Backend✅Chrome Extension✅Notion Integration✅Cloud Deployment✅End-to-End System✅🧠 Debugging LessonsEmpty Notion DB: Ensure the column is named Name (Not "Task" or "Title").Connection Error: Verify the integration is added via Connections, not just "Invite."CORS/Network: Always use the public HTTPS URL from Codespaces for the extension to communicate with the backend.👨‍💻 AuthorDurga Dhanush Yaragani B.Tech Final Year Student | AI & ML Enthusiast
