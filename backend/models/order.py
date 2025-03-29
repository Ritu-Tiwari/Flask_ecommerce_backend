from backend.app import db

class Order(db.Model):
    __tablename__ = "order"  # Table name in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    user_id= db.Column(db.String(100),db.ForeignKey("user.username"), nullable=False)
    amount = db.Column(db.Float, nullable=False)


    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "amount": self.amount}
    
    