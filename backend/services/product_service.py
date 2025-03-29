from backend.app import db
from backend.models.product import Product
from backend.exceptions import ResourceNotFoundException

class ProductService:

    @staticmethod
    def add_product(data):
        new_product = Product(id=data["id"],name=data["name"], price=data["price"])
        db.session.add(new_product)
        db.session.commit()
        return {"message":"Product added", "product details":new_product.to_dict()}
    
    @staticmethod
    def view_product_detail(id):
        product  = Product.query.get(id)
        print(product)
        if not product:
            raise ResourceNotFoundException("Product was not found.Enter valid Id",404)
        return product.to_dict()

    @staticmethod
    def view_all_products():
        products = Product.query.all()
        if not products:
            raise ResourceNotFoundException("No Products available.",404)
        result = [product.to_dict() for product in products]
        return result
       
    @staticmethod
    def update_product(id,data):
        product = Product.query.get(id)
        if not product:
            raise ResourceNotFoundException("Product does not exist.",404)
        if "name" in data:
            product.name =  data["name"]
        if "price" in data:
            product.price = data["price"]
        db.session.commit()
        
        return  "Product was updated successfully"
    
    @staticmethod
    def delete_product(id):
       product  = Product.query.get(id)
       if not product:
            raise ResourceNotFoundException("Product does not exist.",404)
       
       db.session.delete(product)
       db.session.commit()
       return "Product was deleted successfully"
