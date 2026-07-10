from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Trouble Shooting Week 1 Lab")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index():
    return RedirectResponse(url="/ts-week1")


@app.get("/ts-week1", response_class=HTMLResponse)
async def ts_week1(request: Request):
    return templates.TemplateResponse(request, "troubleshooting_week1.html")
