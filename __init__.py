import datetime
from flask import Flask, jsonify, request
from pyrfc import Connection
from models.managedeliveryschedules_model import ManageDeliverySchedule
from models.manageinvoicedetails_model import Invoice
from routes import Create_routes
from default_settings import Create_Database
from extensions import Create_Extension
from default_settings import db 


def Create_app():
    app = Flask(__name__)

    Create_Database(app)
    Create_routes(app)
    Create_Extension(app)

    from blueprints import ulp, slp, dlp
    app.register_blueprint(ulp)
    app.register_blueprint(slp)
    app.register_blueprint(dlp)

    sap_config = {
        'user': 'VEDURUPARTHB',
        'passwd': 'Saibhaskar@2002',
        'ashost': '10.56.7.40',
        'sysnr': '01',
        'client': '100',
        'lang': 'EN',
    }

    @app.route('/sap/porder', methods=['GET'])
    def get_porder():
        try:
            iv_date_low = request.args.get('date_low')
            iv_date_high = request.args.get('date_high')
            if not iv_date_low or not iv_date_high:
                return jsonify({'error': 'date_low and date_high query params required (YYYYMMDD)'}), 400

            conn = Connection(**sap_config)
            result = conn.call('ZRFC_PORDER', IV_DATE_LOW=iv_date_low, IV_DATE_HIGH=iv_date_high)
            
            # Return both export tables directly; PyRFC gives dict and list-of-dict automatically
            response = {
                'ET_PO_HEADER': result.get('ET_PO_HEADER', []),  # structure or table
                'ET_PO_ITEMS': result.get('ET_PO_ITEMS', [])     # table
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    @app.route('/sap/get_delivery_schedule', methods=['POST'])
    def get_delivery_schedule():
        data = request.json
        i_lifnr = data.get('I_LIFNR')
        i_date = data.get('I_DATE')

        try:
            conn = Connection(**sap_config)

            # Prepare parameters dynamically
            params = {}
            if i_date and i_lifnr:
                params['I_DATE'] = i_date
                params['I_LIFNR'] = i_lifnr
            elif i_date:
                params['I_DATE'] = i_date
            elif i_lifnr:
                params['I_LIFNR'] = i_lifnr

            # Call SAP RFC to get delivery schedule
            result = conn.call('ZPO_MANAGE_DELIVERY', **params)
            et_delivery_schedule = result.get('ET_DELIVERY_SCHEDULE', [])

            # Process and save each record into the database
            for record in et_delivery_schedule:
                purchase_order_date = datetime.datetime.strptime(record.get('AEDAT', ''), '%Y%m%d').date() if record.get('AEDAT') else None
                delivery_schedule_date = datetime.datetime.strptime(record.get('EINDT', ''), '%Y%m%d').date() if record.get('EINDT') else None
                delivery_schedule_no = int(record.get('ETENR')) if record.get('ETENR') else None

                schedule = ManageDeliverySchedule(
                    supplier_name=record.get('NAME1', ''),
                    purchase_order_no=record.get('EBELN', ''),
                    purchase_order_date=purchase_order_date,
                    delivery_schedule_no=delivery_schedule_no,
                    delivery_schedule_date=delivery_schedule_date,
                    created_by='system',
                    created_date=datetime.datetime.now()
                )
                db.session.add(schedule)

            db.session.commit()

            return jsonify({"ET_DELIVERY_SCHEDULE": et_delivery_schedule})

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @app.route('/sap/get_invoice_details', methods=['POST'])
    def get_invoice_details():
        data = request.json
        i_lifnr = data.get('I_LIFNR')
        i_date = data.get('I_DATE')

        try:
            conn = Connection(**sap_config)

            params = {}
            if i_date and i_lifnr:
                params['I_DATE'] = i_date
                params['I_LIFNR'] = i_lifnr
            elif i_date:
                params['I_DATE'] = i_date
            elif i_lifnr:
                params['I_LIFNR'] = i_lifnr

            result = conn.call('Z_GET_INVOICE_DETAILS', **params)
            et_invoice_details = result.get('ET_INVOICE_DETAILS', [])

            for record in et_invoice_details:
                invoice_date = datetime.datetime.strptime(record.get('BUDAT', ''), '%Y%m%d').date() if record.get('BUDAT') else None

                invoice = Invoice(
                    supplier_code=record.get('LIFNR', ''),
                    supplier_name=record.get('NAME1', ''),
                    purchase_order_no=record.get('EBELN', ''),
                    invoice_no=record.get('BELNR', ''),
                    invoice_date=invoice_date
                )
                db.session.add(invoice)

            db.session.commit()

            return jsonify({"ET_INVOICE_DETAILS": et_invoice_details})

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    return app
