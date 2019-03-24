from flask import Blueprint

api = Blueprint('api', __name__)

# Always at bottom to avoid circular dependencies.
from app.api import authentication, detections, errors
