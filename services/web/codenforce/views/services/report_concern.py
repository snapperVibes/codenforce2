from os import path
from typing import Optional

import fastapi
from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.engine.base import Connection

from .. import templates


router = fastapi.APIRouter()


def url(name: str) -> str:
    return "/services/report_concern/" + name


def file(name: str) -> str:
    return path.join("services", "report_concern", name)


@router.get(url(""))
async def root():
    return RedirectResponse(url("address"))


# TODO: Figure out naming schema so names don't shadow each other
# TODO: Figure out how to refactor address selection somewhere else
@router.get(url("address"))
async def address(r: Request, address: Optional[str] = None):
    results = None
    if address:
        results = query_addresses(r.app.state.db, address)
    return templates.TemplateResponse(
        file("address.html"), {"request": r, "results": results}
    )


def query_addresses(address: str, conn: Connection):
    address = parse.address(address)


@router.get(url("describe"), response_class=HTMLResponse)
async def select_parcel(r: Request, address: str):

    return templates.TemplateResponse(file("describe.html"), {"request": r})
