from flask import Flask, jsonify, request
from pyrfc import Connection
from routes import Create_routes
from default_settings import Create_Database
from extensions import Create_Extension

def Create_app():
    app = Flask(__name__)

    Create_Database(app)
    Create_routes(app)
    Create_Extension(app)

    from blueprints import ulp, slp
    app.register_blueprint(ulp)
    app.register_blueprint(slp)

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

    return app
