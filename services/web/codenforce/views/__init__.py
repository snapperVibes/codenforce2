from os import path

from fastapi.templating import Jinja2Templates

HERE = path.dirname(path.realpath(__file__))

templates = Jinja2Templates(directory=path.join(HERE, "..", "templates"))

__all__ = [
    "templates",
]
