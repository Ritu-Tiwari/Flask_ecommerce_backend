from backend.app import db

class Product(db.Model):
    __tablename__ = "product"  # Table name in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100),unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)


    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}
    
    