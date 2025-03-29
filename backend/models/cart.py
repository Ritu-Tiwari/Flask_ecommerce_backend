from backend.app import db

class Cart(db.Model):
    __tablename__ = "cart"  # Table name in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id= db.Column(db.String(100),db.ForeignKey("user.username"), nullable=False)
    product = db.Column(db.String(100), db.ForeignKey("product.name"),nullable=False)
    quantity = db.Column(db.Integer)
    


    def to_dict(self):
        return {"id": self.id,"product":self.product, "quantity":self.quantity}
    
    