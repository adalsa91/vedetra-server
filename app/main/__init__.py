from flask import Blueprint

main = Blueprint('main', __name__)

# Always at bottom to avoid circular dependencies.
from . import views, errors
