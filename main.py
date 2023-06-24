import uvicorn
from fastapi import FastAPI
from fastapi import Request 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# app.mount("/templates", StaticFiles(directory="templates"), name="static")

templates = Jinja2Templates(directory="templates")





@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, port=8000)