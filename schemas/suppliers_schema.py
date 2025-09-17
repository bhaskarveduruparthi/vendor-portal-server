from marshmallow import Schema , fields
from models.suppliers_model import Supplier

class Supplier_Schema(Schema):
    class Meta:
        model = Supplier
        ordered = True
        
        exclude = ("password",  )

    id = fields.Integer()
    suppliername = fields.String(required=True)
    suppliercode = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    loginid = fields.Integer(required=True)
    contact_person = fields.String(required=True)
    landline_number = fields.String(required=True)
    mobile_number = fields.String(required=True)
    city = fields.String(required=True)



supplier = Supplier_Schema()
suppliers = Supplier_Schema(many=True)