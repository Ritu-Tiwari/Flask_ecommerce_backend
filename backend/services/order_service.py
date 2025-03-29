from backend.models.cart import Cart
from backend.models.order import Order
from backend.models.product import Product
from backend.app import db

class OrderService:
    @staticmethod
    def place_order(user_id):
        cart_items = Cart.query.filter_by(user_id=user_id).all()
        if cart_items:
            amount = 0
            for cart_item in cart_items:
                item = cart_item.to_dict()
                product_in_cart = item["product"]
                product = Product.query.filter_by(name= product_in_cart).first()
                amount += product.price*item["quantity"]
            order = Order(user_id=user_id,amount = amount)
            new_order = order.to_dict()
            db.session.add(order)
            db.session.commit()

        #flush out the ordered items from user cart
            for cart_item in cart_items:
                db.session.delete(cart_item)
                db.session.commit()
            return {"order_details":new_order,"message":"Order Placed Successfully"}
        return "Empty Cart. Add items to Place order"

