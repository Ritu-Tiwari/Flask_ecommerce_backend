from backend.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User (db.Model):
    __tablename__ = "user"
    username = db.Column(db.String(50), primary_key = True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        user = {
            "username":self.username,
            "email":self.email
        }
        return user

   
    
