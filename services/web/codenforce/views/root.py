import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from . import templates
import sys

# Todo: Find Pythonic import method
sys.path.append("..")
import db

router = fastapi.APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(r: Request):
    return RedirectResponse(url="/home")


@router.get("/home", response_class=HTMLResponse)
async def home(r: Request):
    return templates.TemplateResponse("home.html", {"request": r})


@router.get("/login", response_class=HTMLResponse)
async def login(r: Request):
    return templates.TemplateResponse("login.html", {"request": r})

