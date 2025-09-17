from default_settings import db 

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loginid = db.Column(db.String(length=200), unique=True, nullable=False)
    firstname = db.Column(db.String(length=200), nullable=False)
    lastname = db.Column(db.String(length=200), nullable=False)
    email = db.Column(db.String(length=200), unique=True, nullable=False)
    password = db.Column(db.String(length=100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    


    def  __init__(self,loginid, firstname, lastname, email, password):

       
        self.email = email,
        self.firstname = firstname,
        self.lastname = lastname,
        self.password = password,
        self.loginid = loginid
      