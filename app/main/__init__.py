from flask import Blueprint
main = Blueprint('main',__name__)

#initialise views and errors in main
from . import views, errors