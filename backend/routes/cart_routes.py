from flask import Blueprint, jsonify, request,g
from backend.services.cart_service import CartService
from backend.services.auth_service import AuthService
from backend.exceptions import  InvalidCredentialsException, ResourceNotFoundException

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/", methods=["GET"])
@AuthService.login_required
def get_cart():
    try:
        result = CartService.get_cart(g.user)

        return jsonify ({"message":result}, 200)
    

    except Exception as e :
        return jsonify({"error": str(e)})

    
@cart_bp.route("/", methods=["POST","PUT"])
@AuthService.login_required
def add_to_cart():
    data = request.json
    if not data or "product" not in data:
        return jsonify({"error":"Invalid data"}), 404
    try:
        result = CartService.add_to_cart(g.user,data)
        return jsonify({"message":result})
    
    except ResourceNotFoundException as e:
        return jsonify({"error": e.message}), e.status_code
    
    except Exception as e :
        return jsonify({"error": str(e)})

@cart_bp.route("/<int:id>", methods=["DELETE"])
@AuthService.login_required
def remove_from_cart(id):
    try:
        result = CartService.remove_from_cart(id)
        return jsonify({"message":result})
    

    except Exception as e :
        return jsonify({"error": str(e)})
    

