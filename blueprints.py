from flask import Blueprint

ulp = Blueprint('users', __name__, url_prefix='/users')

slp = Blueprint('suppliers', __name__, url_prefix='/suppliers')




