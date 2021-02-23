from os import path

from fastapi.templating import Jinja2Templates

HERE = path.dirname(path.realpath(__file__))

templates = Jinja2Templates(directory=path.join(HERE, "..", "templates"))

import sys

sys.path.append("..")
import parse

__all__ = ["templates", "parse"]
