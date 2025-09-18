from default_settings import db 

class ManageDeliverySchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(255), nullable=False)
    purchase_order_no = db.Column(db.String(50), nullable=False)
    purchase_order_date = db.Column(db.Date, nullable=False)
    delivery_schedule_no = db.Column(db.Integer, nullable=False)
    delivery_schedule_date = db.Column(db.Date, nullable=False) 
    created_by = db.Column(db.String(100), nullable=True)
    created_date = db.Column(db.DateTime, nullable=True)
    last_updated_date = db.Column(db.DateTime, nullable=True)
    last_updated_by = db.Column(db.String(100), nullable=True)


