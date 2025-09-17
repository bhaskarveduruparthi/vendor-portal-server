from flask import request, json , jsonify
from extensions.BCRYPT import bcrypt
from flask_restful import Resource
from models.users_model import User
from schemas.users_schema import user,users
from default_settings import db 
from blueprints import ulp
import datetime
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


class User_Auth(Resource):


    @ulp.route('/login', methods=['POST'])
    def login_user():

        data = request.get_json()
        loginid = data['loginid']
        password = data['password']

        post = User.query.filter_by(loginid=loginid).first()

        expires = datetime.timedelta(minutes=60)

        if post and bcrypt.check_password_hash(post.password,password):
           access_token = create_access_token(identity=loginid, expires_delta=expires)
           return jsonify({'access_token': access_token})
        else:
           return jsonify({'message': 'Invalid credentials'}), 401
        

    @ulp.route('/create_admin', methods=['POST'])
    def create_admin():
    # Extract data from JSON payload
        firstname = request.json.get('firstname')
        lastname = request.json.get('lastname')
        email = request.json.get('email')
        password = request.json.get('password')
        
        # Validate required fields are present (optional but recommended)
        if not firstname or not lastname or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        # Create User instance
        admin_user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,  # will overwrite below with hash
            loginid='Admin'
        )
        
        # Hash the password before storing it
        admin_user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Add user to session and commit to DB
        db.session.add(admin_user)
        db.session.commit()
        
        return jsonify({"message": "Admin Created Successfully"}), 201

    

    @ulp.route('/changepassword', methods=['POST'])
    @jwt_required()
    def change_password():
        
        current_user = get_jwt_identity()

        check_user = User.query.filter_by(loginid=current_user).first()



        if check_user is not None:

            data = request.get_json()
            old_password = data.get('old_password')
            new_password = data.get('new_password')
            retype_password = data.get('retype_password')


           
            if bcrypt.check_password_hash(check_user.password, old_password):

                hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
                check_user.password = hashed_password
                db.session.commit()

                return jsonify("Password changed")
            
            else:
                return jsonify("Missing Credentials"),500
         
        else:
            return jsonify("User not found"),400
        
