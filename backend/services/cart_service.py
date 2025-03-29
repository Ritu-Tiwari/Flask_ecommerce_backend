from backend.models.cart import Cart
from backend.models.product import Product
from backend.exceptions import ResourceNotFoundException
from backend.app import db

class CartService:

    @staticmethod
    def get_cart(user_id):
       
        cart_items = Cart.query.filter_by(user_id = user_id).all()
    
        if not cart_items:
            return "Your Cart is empty"
        result = [cart_item.to_dict() for cart_item in cart_items]
        return result

    @staticmethod
    def add_to_cart(user_id,data):
        product = Product.query.filter_by(name = data["product"]).first()
        if not product:
            raise ResourceNotFoundException("The requested product does not exist", 404)
        cart_item = Cart.query.filter_by(user_id = user_id, product = data["product"]).first()
        if not cart_item:
            new_item= Cart(user_id=user_id, product=data["product"], quantity = 1)
            db.session.add(new_item)
            db.session.commit()
            return "Item was added successfully"
        cart_item.quantity += 1
        db.session.commit()
        return "Item was added successfully"
    
    @staticmethod
    def remove_from_cart(id):
        cart_item = Cart.query.filter_by(id=id).first()
        db.session.delete(cart_item)
        db.session.commit()
        return "Item deleted from your cart"

        
        
        


                