from backend.app import db
from backend.models.user import User
from werkzeug.security import check_password_hash
from functools import wraps
from flask import request, jsonify, g
import datetime
from backend.exceptions import InvalidCredentialsException, ResourceNotFoundException

class AuthService:

    @staticmethod
    def register_user(user):
        username = user['username']
        password = user['password']
        email = user['email']

        user = User(username = username, email = email)
        new_user = user.to_dict()
        user.set_password(password)
        

        db.session.add(user)
        db.session.commit()
        return {"user details":new_user,"message":"User registered successfully"}
        
        
    @staticmethod
    def login_user (data):
        user_record = User.query.filter_by(username = data["username"]).first()
        if not user_record:
            raise ResourceNotFoundException("User not Found. Register with us.",404)
        if not user_record.check_password(data["password"]):
            raise InvalidCredentialsException("Invalid credential. Please check username and password", 401)
    
        return {"user details":user_record.to_dict(),"message":"User logged in"}
            
            
    
    @staticmethod  
    def login_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            
            auth = request.headers.get("Authorization")
    
            if not auth:
                return jsonify({"error": "Missing Authentication Code"}),401
            
            import base64
            credentials = auth.split(' ')[1]
            credentials = base64.b64decode(credentials).decode('utf-8')
            username, password = credentials.split(':',1)
            if  not username or not password:
                return jsonify({"error": "Missing Credentials"}),401
            user = User.query.get(username) 
            if not user or not user.check_password(password):
                return jsonify({"error": "Invalid Credentials"}),401
            g.user = user.username
            
            return f(*args, **kwargs)

        return decorated


