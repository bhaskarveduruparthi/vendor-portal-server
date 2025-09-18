from resources.users_views import User_Requirements
from resources.suppliers_views import Supplier_Requirements
from resources.auth_login import User_Auth
from resources.getdata_sap_views import SapData_Requirements
from flask_restful import Api



def Create_routes(app):

    api = Api(app)

    api.add_resource(User_Auth, '/users', methods=['GET','POST'])
    api.add_resource(User_Requirements, '/users', methods=['GET','POST', 'PUT', 'DELETE'])
    api.add_resource(Supplier_Requirements, '/suppliers', methods=['GET','POST', 'PUT', 'DELETE'])
    api.add_resource(SapData_Requirements, '/sapdata', methods=['GET','POST', 'PUT', 'DELETE'] )
    return api.init_app(app)