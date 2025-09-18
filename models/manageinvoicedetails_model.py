from default_settings import db

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_code = db.Column(db.String(20), nullable=False)
    supplier_name = db.Column(db.String(100), nullable=False)
    purchase_order_no = db.Column(db.String(50), nullable=False)
    invoice_no = db.Column(db.String(50), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
