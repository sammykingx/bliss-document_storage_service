from flask import Blueprint

bp = Blueprint("support", __name__)

from . import dev_support