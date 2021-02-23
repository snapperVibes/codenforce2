from os import path
from typing import Optional, Dict, NamedTuple

import fastapi
from fastapi import Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import text
from sqlalchemy.engine.base import Engine

from .. import templates, parse


router = fastapi.APIRouter()


def url(name: str) -> str:
    return "/services/report_concern/" + name


def file(name: str) -> str:
    return path.join("services", "report_concern", name)


@router.get(url(""))
async def root():
    return RedirectResponse(url("address"))


class AddressAndParcel(NamedTuple):
    address: str
    parcel: str


# TODO: Figure out naming schema so names don't shadow each other
# TODO: Figure out how to refactor address selection somewhere else
@router.get(url("address"))
async def address(r: Request, address: Optional[str] = None):
    results = None
    if address:
        # Temp parcel for testing
        # results = [AddressAndParcel(address=address, parcel="0373H00185000000"), AddressAndParcel(address="123 Example St, CogLand, PA", parcel="PARCEL")]
        address_parts = parse.address(address)
        addresses = query_addresses(address_parts, r.app.state.db)
        results = [
            {"address": concat_address(row), "parcel": row.parid} for row in addresses
        ]
    return templates.TemplateResponse(
        file("address.html"), {"request": r, "results": results}
    )


@router.get(url("describe"), response_class=HTMLResponse)
async def describe(r: Request, parcel: str):
    # We hit the database an extra time here: Todo: Optimize
    parcel_data = query_parcel(parcel, r.app.state.db)
    issues = query_issue_type(r.app.state.db)
    return templates.TemplateResponse(file("describe.html"), {"request": r, "issues": issues, "parcel_data": parcel_data})


@router.get(url("photo"), response_class=HTMLResponse)
async def photo(r: Request, parcel: str):
    parcel_data = query_parcel(parcel, r.app.state.db)
    return templates.TemplateResponse(file("photo.html"), {"request": r, "parcel_data": parcel_data})


@router.get(url("contact"), response_class=HTMLResponse)
async def contact(r: Request):
    return templates.TemplateResponse(file("contact.html"), {"request": r})


@router.get(url("review_and_submit"), response_class=HTMLResponse)
async def contact(r: Request):
    return templates.TemplateResponse(file("review_and_submit.html"), {"request": r})


########################################################################################
def concat_address(a) -> str:
    return f"{a.propertyhousenum} {a.propertyaddress}\n{a.propertycity}, {a.propertystate} {a.propertyzip}"


def query_addresses(address: Dict[str, Optional[str]], engine: Engine):
    with engine.connect() as conn:
        statement = text(
            "SELECT parid, propertyhousenum, propertyaddress, propertycity, propertystate, propertyunit, propertyzip, municode FROM externalwprdc WHERE propertyhousenum = :housenumber and propertyaddress = :address LIMIT 10"
        )
        print("HERE WE GO", address)
        query = conn.execute(statement, address)
        return query.all()


# Todo: LRU cache?
def query_parcel(parcel_id: str, engine: Engine):
    with engine.connect() as conn:
        statement = text(
            "SELECT propertyhousenum, propertyaddress, munidesc, parid FROM externalwprdc "
            "WHERE parid = :parcel_id"
        )
        query = conn.execute(statement, {"parcel_id": parcel_id})
        return query.all()[0]    # Todo: Fetchone and validation


def query_issue_type(engine: Engine):
    with engine.connect() as conn:
        statement = text(
            "SELECT typename, typedescription FROM ceactionrequestissuetype"
        )
        query = conn.execute(statement)
        return query.all()