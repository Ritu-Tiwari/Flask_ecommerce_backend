from flask import Blueprint,request, jsonify,g

from backend.services.auth_service import AuthService
from backend.services.order_service import OrderService
from backend.exceptions import InvalidCredentialsException


order_bp = Blueprint("order", __name__)

@order_bp.route("/", methods=["POST"])
@AuthService.login_required
def place_order():

    try:
        result = OrderService.place_order(g.user)
        return jsonify (result), 201
    
    except Exception as e :
        return jsonify({"error": str(e)})

