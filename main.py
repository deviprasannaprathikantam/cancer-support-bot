from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from openai_helper import get_cancer_support_response

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": []})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    bot_reply = get_cancer_support_response(message)
    conversation = [
        
        {"role": "user", "content": message},
        {"role": "bot", "content": bot_reply}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "response": conversation})