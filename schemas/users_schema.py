from marshmallow import Schema , fields
from models.users_model import User

class User_Schema(Schema):
    class Meta:
        model = User
        ordered = True
        dateformat = '%Y-%m-%d'
        exclude = ("password",  )

    id = fields.Integer()
    firstname = fields.String(required=True)
    lastname = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    loginid = fields.String(required=True)


user = User_Schema()
users = User_Schema(many=True)