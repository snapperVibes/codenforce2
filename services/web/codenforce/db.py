import os
from typing import Dict, Optional, Any, Type

from sqlalchemy import Column, create_engine, Integer, Identity, Table
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.dialects.postgresql import TEXT

# Monkey patch the declarative base to add our own


def init_engine() -> Engine:
    # Create URI (Connection string)
    # https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    # dbname = os.getenv("POSTGRES_DB")
    dbname = "cogdb"
    port = os.getenv("POSTGRES_PORT")
    host = os.getenv("POSTGRES_HOST")
    uri = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return create_engine(uri, future=True)


def table_mapper(table: DeclarativeMeta) -> Dict[str, Any]:
    """ Maps table columns into a dictionary """
    return dict((column.name, None) for column in table().__table__.c)


Model = declarative_base(name="Model")


class Address(Model):
    __tablename__ = "address"

    id = Column(Integer, Identity(), primary_key=True)
    # Let's ignore gridzone for now
    crossstreet = Column(TEXT)
    number = Column(TEXT)
    prefixdirection = Column(TEXT)
    street = Column(TEXT)
    suffixdirection = Column(TEXT)
    type = Column(TEXT)
    city: Column(TEXT)
    borough: Column(TEXT)
    state: Column(TEXT)
    zip: Column(Integer)
    four: Column(Integer)
