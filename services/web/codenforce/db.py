import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection

# class CodeNforceConnection(Connection):
#     def __init__(self, engine, *args, **kwargs):
#         super(CodeNforceConnection, self).__init__(engine, *args, **kwargs)


def connect() -> Connection:
    # Create URI (Connection string)
    # https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    # dbname = os.getenv("POSTGRES_DB")
    dbname = "cogdb"
    port = os.getenv("POSTGRES_PORT")
    host = os.getenv("POSTGRES_HOST")
    uri = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    engine = create_engine(uri)
    return engine.connect()
