from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(testing):

    app =  Flask(__name__)
    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory DB for testing
        app.config["TESTING"] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False
    

    db.init_app(app)
    from backend.routes.user_routes import user_bp
    from backend.routes.product_routes import product_bp
    from backend.routes.cart_routes import cart_bp
    from backend.routes.order_routes import order_bp
    app.register_blueprint(user_bp, url_prefix = "/users")
    app.register_blueprint(product_bp, url_prefix = "/products")
    app.register_blueprint(cart_bp, url_prefix = "/cart")
    app.register_blueprint(order_bp, url_prefix ="/checkout")

    from backend.models.user import User
    from backend.models.product import Product
    from backend.models.cart import Cart
    from backend.models.order import Order


    with app.app_context():
        db.create_all()

    return app