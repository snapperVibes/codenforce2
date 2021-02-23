import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import db
from views import root
from views.services import report_concern

HERE = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()


@app.on_event("startup")
async def startup():
    # Connect to the database and at it to the app's shared state.
    app.state.db = db.init_engine()

    # Include URL routes
    app.include_router(root.router)
    app.include_router(report_concern.router)

    app.mount(
        "/static", StaticFiles(directory=os.path.join(HERE, "static")), name="static"
    )


# For development
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
