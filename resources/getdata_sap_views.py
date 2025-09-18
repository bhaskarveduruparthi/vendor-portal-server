from flask import request, json , jsonify
from extensions.BCRYPT import bcrypt
from flask_restful import Resource
from models.users_model import User
from models.managedeliveryschedules_model import ManageDeliverySchedule
from models.manageinvoicedetails_model import Invoice
from schemas.users_schema import user,users
from schemas.managedeliveryschedules_schema import deliveryschedule, deliveryschedules
from schemas.manageinvoicedetails_schema import invoice_schema, invoices_schema
from default_settings import db 
from blueprints import dlp
from flask_jwt_extended import get_jwt_identity, jwt_required


class SapData_Requirements(Resource):


    
    @dlp.route('/managedeliveryschedules', methods=['GET'])
    @jwt_required()
    def get_all_deliveryschedules():
            
            current_user = get_jwt_identity()
            check_user = User.query.filter_by(loginid=current_user).first()

            

            if check_user.loginid == 'SuperAdmin' or 'Admin':
                
                posts = ManageDeliverySchedule.query.all()
                result = deliveryschedules.dump(posts)
                return jsonify(result)
            
            else:
                return jsonify("Not Authorized")
            
    @dlp.route('/manageinvoicedetails', methods=['GET'])
    @jwt_required()
    def get_all_invoicedetails():
            
            current_user = get_jwt_identity()
            check_user = User.query.filter_by(loginid=current_user).first()

            

            if check_user.loginid == 'SuperAdmin' or 'Admin':
                
                posts = Invoice.query.all()
                result = invoices_schema.dump(posts)
                return jsonify(result)
            
            else:
                return jsonify("Not Authorized")