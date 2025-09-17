from default_settings import db 


class Supplier(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loginid = db.Column(db.String(length=200), unique=True, nullable=False)
    suppliercode = db.Column(db.String(length=200), nullable=False)
    contact_person = db.Column(db.String(length=200), nullable=False)
    landline_number = db.Column(db.String(length=200), nullable=False)
    mobile_number = db.Column(db.String(length=200), nullable=False)
    city = db.Column(db.String(length=200), nullable=False)
    suppliername = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=200), unique=True, nullable=False)
    password = db.Column(db.String(length=100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    


    def  __init__(self,loginid, suppliername, suppliercode, contact_person, city, landline_number, mobile_number, email, password):

       
        self.email = email,
        self.suppliername = suppliername,
        self.suppliercode = suppliercode,
        self.city = city,
        self.landline_number = landline_number,
        self.mobile_number = mobile_number,
        self.contact_person = contact_person
        self.password = password,
        self.loginid = loginid
      