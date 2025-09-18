from marshmallow import Schema, fields
from models.managedeliveryschedules_model import ManageDeliverySchedule


class ManageDeliveryScheduleSchema(Schema):
    class Meta:
        model = ManageDeliverySchedule
        ordered = True
        exclude = ()

    id = fields.Integer()
    supplier_name = fields.String(required=True)
    purchase_order_no = fields.String(required=True)
    purchase_order_date = fields.Date(required=True)
    delivery_schedule_no = fields.Integer(required=True)
    delivery_schedule_date = fields.Date(required=True)
    created_by = fields.String()
    created_date = fields.Date()
    last_updated_date = fields.Date()
    last_updated_by = fields.String()

deliveryschedule = ManageDeliveryScheduleSchema()
deliveryschedules = ManageDeliveryScheduleSchema(many=True)
