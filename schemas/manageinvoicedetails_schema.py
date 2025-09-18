from marshmallow import Schema, fields
from models.manageinvoicedetails_model import Invoice


class InvoiceSchema(Schema):
    class Meta:
        ordered = True
        model = Invoice  
        exclude = ()

    id = fields.Integer()
    supplier_code = fields.String(required=True)
    supplier_name = fields.String(required=True)
    purchase_order_no = fields.String(required=True)
    invoice_no = fields.String(required=True)
    invoice_date = fields.Date(required=True)

invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)
