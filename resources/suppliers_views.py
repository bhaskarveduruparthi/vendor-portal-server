from flask import request, json , jsonify
from extensions.BCRYPT import bcrypt
from flask_restful import Resource
from models.suppliers_model import Supplier
from schemas.suppliers_schema import supplier, suppliers
from default_settings import db 
from blueprints import slp
from flask_jwt_extended import get_jwt_identity, jwt_required


class Supplier_Requirements(Resource):


    def getsuppliers():
        return 