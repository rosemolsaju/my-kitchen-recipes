from flask import Blueprint

recipes1_blueprint = Blueprint('recipes1', __name__, template_folder='templates')

# Import the routes module
from . import routes

