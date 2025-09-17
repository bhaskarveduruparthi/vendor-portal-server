from flask import request, json , jsonify
from extensions.BCRYPT import bcrypt
from flask_restful import Resource
from models.users_model import User
from schemas.users_schema import user,users
from default_settings import db 
from blueprints import ulp
from flask_jwt_extended import get_jwt_identity, jwt_required


class User_Requirements(Resource):


    @ulp.route('/getuser', methods=['GET'])
    @jwt_required()
    def getuser():

        current_user = get_jwt_identity()

        get_user = User.query.filter_by(loginid=current_user).first()

        result = user.dump(get_user)
        return jsonify(result)

    @ulp.route('/getallusers', methods=['GET'])
    @jwt_required()
    def get_all_users():
            
            current_user = get_jwt_identity()
            check_user = User.query.filter_by(loginid=current_user).first()

            page = request.args.get('page',1, type=int)

            if check_user.loginid == 'SuperAdmin':
                
                posts = User.query.paginate(page=page, per_page=10)
                result = users.dump(posts)
                return jsonify(result)
            
            else:
                return jsonify("Not Authorized")