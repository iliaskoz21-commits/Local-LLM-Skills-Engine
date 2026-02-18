# Multi-Skill LLM Framework: A New Approach to Local AI 🚀

This project demonstrates a modular approach to interacting with Local LLMs (Large Language Models) using **Ollama**. Instead of generic interactions, it uses a specialized "Skills" architecture to transform the AI into different professional personas instantly.

## 🌟 Key Features
- **The "Skills" Concept**: Dynamically load System Prompts from Markdown files to change the AI's behavior and expertise.
- **Local & Private**: Powered by **Ollama**, ensuring all data stays on your machine (Mistral/Llama3/Phi3).
- **Professional Setup**: Includes Environment Variables (.env), dependency management, and a modular Python architecture.
- **Streaming Output**: Provides a real-time, responsive terminal experience.

## 🛠 Tech Stack
- **Language**: Python 3.x
- **LLM Runner**: [Ollama](https://ollama.com/)
- **Core Libraries**: `ollama-python`, `python-dotenv`

## 📂 Project Structure
```text
ollama_skills/
├── skills/             # Collection of specialized mentor profiles (.md)
├── .env                # Local configuration (Ignored by Git)
├── .env.example        # Template for environment variables
├── .gitignore          # Rules for Git (excludes venv and secrets)
├── app.py              # Main application logic
└── requirements.txt    # Project dependencies
🚀 Quick Start
1. Prerequisites
Ensure you have Ollama installed and the Mistral model pulled:

Bash
ollama pull mistral
2. Installation
Clone the repository and set up your environment:

PowerShell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements (using the python -m bypass for Windows Policy)
python -m pip install -r requirements.txt
3. Configuration
Create your .env file from the example:

PowerShell
cp .env.example .env
Edit .env and set your MODEL_NAME=mistral:latest.

4. Running the App
PowerShell
python app.py
🧠 How it Works
The application scans the /skills directory for Markdown files. Each file acts as a "personality" or "expert" module. By selecting a skill, the system injects those instructions as a System Message, forcing the LLM to adhere to specific professional guidelines and languages.

Created as part of my transition from IT Education to AI Engineering.