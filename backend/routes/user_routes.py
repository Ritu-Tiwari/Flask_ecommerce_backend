from flask import Blueprint, request, jsonify
from backend.services.auth_service import AuthService
from backend.exceptions import ResourceNotFoundException, InvalidCredentialsException

user_bp =  Blueprint("users", __name__)


@user_bp.route('',methods=['POST'])
def register():
    data = request.json
    if not data or "username" not in data or "email" not in data or "password" not in data:
        return jsonify({"error": "Invalid data"}), 400 
    try:
        result =AuthService.register_user(data)
        return jsonify (result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@user_bp.route('', methods =['GET'])
def login():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid data"}), 400 
    try :
        result = AuthService.login_user(data)
        return jsonify(result),200
    
    except ResourceNotFoundException as e:
        return jsonify({"error": e.message}), e.status_code
    
    except InvalidCredentialsException as e:
        return jsonify({"error": e.message}), e.status_code
    
    except Exception as e:
        return jsonify({"error":str(e)}), 400



