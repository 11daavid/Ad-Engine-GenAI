import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from groq import Groq

load_dotenv()

app = FastAPI()
app.mount("/static_outputs", StaticFiles(directory="."), name="static")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Hugging Face Settings (English)
HF_API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
HF_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Verificăm dacă fișierul există înainte să-l citim
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Eroare: Fisierul index.html nu a fost gasit in folderul proiectului!</h1>"

@app.get("/generate-full-ad")
def generate_full_ad(produs: str, public_tinta: str = "tineri"):
    prompt_sistem = ("You are a marketing expert. Respond ONLY in JSON format with: title, hook, description, cta. Language: Romanian.")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_sistem},
            {"role": "user", "content": f"Product: {produs}, Target: {public_tinta}"}
        ],
        model="llama-3.3-70b-versatile",
        response_format={"type": "json_object"}
    )
    import json
    ad_data = json.loads(chat_completion.choices[0].message.content)
    image_prompt = f"A professional studio product photo of a {produs}, minimalist, 4k, premium"
    img_response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": image_prompt})
    if img_response.status_code == 200:
        with open("final_ad_image.png", "wb") as f:
            f.write(img_response.content)
        ad_data["image_status"] = "Success"
    else:
        ad_data["image_status"] = "Error or Loading"
        

    
    history_entry = {
        "produs": produs,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Succes" if img_response.status_code == 200 else "Eșuat",
        "image_path": "file_ad_image.png" if img_response.status_code == 200 else None
    }

    history_file = "history.json"
    history_data = []
    
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            try:
                history_data = json.load(f)
            except:
                history_data = []

    history_data.append(history_entry)

    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history_data, f, indent=4, ensure_ascii=False)
    
 
    return ad_data

@app.get("/history")
def get_history():
    if os.path.exists("history.json"):
        with open("history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []