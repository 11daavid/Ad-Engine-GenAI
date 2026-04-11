# 🚀 AI Ad Engine - GenAI Marketing Automation

A modern, full-stack web application that leverages Large Language Models (LLMs) and Diffusion Models to automate the creation of professional advertising copy and visual assets. 

## 🌟 Features

- **Automated Copywriting**: Generates compelling ad hooks, body text, and Call-to-Actions (CTAs) using **Llama 3** (via Groq API).
- **Visual Asset Generation**: Creates high-quality, context-aware marketing images using **Stable Diffusion** (via HuggingFace).
- **Persistence**: Tracks generation history locally using a JSON-based storage system.
- **Modern UI**: A responsive, clean dashboard built with a professional business aesthetic.
- **RESTful API**: Built with **FastAPI**, featuring automatic Swagger documentation.

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, FastAPI, Uvicorn.
- **AI/ML**: 
  - **Text**: Llama 3 (Inference via Groq for low latency).
  - **Images**: Stable Diffusion XL (Inference via HuggingFace API).
- **Frontend**: HTML5, CSS3 (Modern Flexbox layout), JavaScript (Fetch API).
- **Environment**: Python Virtual Environments (venv), Dotenv for secret management.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher installed.
- API Keys for [Groq](https://wow.groq.com/) and [HuggingFace](https://huggingface.co/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/11daavid/Ad-Engine-GenAI.git](https://github.com/11daavid/Ad-Engine-GenAI.git)
   cd Ad-Engine-GenAI


2. Create and activate a virtual environment:


python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate


3.Install dependencies:

pip install fastapi uvicorn python-dotenv groq requests




4.Configure environment variables:

GROQ_API_KEY=your_actual_key_here
HUGGINGFACE_API_KEY=your_actual_key_here



Running the Application
Start the FastAPI server:

uvicorn main:app --reload


Access the dashboard at: http://127.0.0.1:8000

Access the API Documentation at: http://127.0.0.1:8000/docs


📂 Project Structure

main.py: The core FastAPI application and AI orchestration logic.

index.html: The interactive dashboard.

history.json: Local data store for generated ads.

.env.example: Template for required security credentials.

.gitignore: Ensures sensitive data and environment files are not tracked.



📝 License
This project was developed for educational and portfolio purposes. Feel free to use and modify it!


