from flask import Blueprint


bp = Blueprint("app_doc", __name__)

from . import staff_doc