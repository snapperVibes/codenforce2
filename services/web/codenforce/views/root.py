import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from . import templates


router = fastapi.APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(r: Request):
    return RedirectResponse(url="/login")


@router.get("/login", response_class=HTMLResponse)
async def home(r: Request):
    return templates.TemplateResponse("login.html", {"request": r})
