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
