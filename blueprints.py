from flask import Blueprint

ulp = Blueprint('users', __name__, url_prefix='/users')

slp = Blueprint('suppliers', __name__, url_prefix='/suppliers')

dlp = Blueprint('sapdata', __name__, url_prefix='/sapdata')




