import requests
from flask import jsonify, make_response, current_app, request

from app.main import bp


@bp.route('/ping', methods=['POST'])
def nlu_service():

    try:
        # READ REQUEST PARAMETERS
        hello = request.json['hello']
        
        # READ CONFIG ENV VARS
        minha_env_var = current_app.config['MINHA_ENV_VAR']
        
        # API BUSINESS LOGIC
        # TODO
        response = {
        	"text": "Hello from your container!",
        	"minha_env_var": minha_env_var
        }
        
    except Exception as err:
        # RETURN SERVICE RESPONSE (IN CASE OF EXCEPTION)
        return make_response(jsonify({"err": True, "msg": "Internal Server Error: {}".format(err)}), 500)
    
    else:
        # RETURN SERVICE RESPONSE (IN CASE OF SUCCESS)
        return make_response(jsonify({"err": False, "data": response}), 200)

