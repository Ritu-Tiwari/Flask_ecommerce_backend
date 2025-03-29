from flask import request, Blueprint, jsonify
from backend.services.product_service import ProductService
from backend.exceptions import ResourceNotFoundException

product_bp = Blueprint("products", __name__)

@product_bp.route('', methods=['GET'])
def get_products():
    try :
        result = ProductService.view_all_products()
        return jsonify (result), 201
    except ResourceNotFoundException as e:
        return jsonify({"error":e.message}), e.status_code
    except Exception as e:
        return jsonify({"error":str(e)}), 400


@product_bp.route("/<int:id>", methods=["GET"])
def get_specific_product(id):
    if not id:
        return jsonify({"error":"Invalid data"}), 404

    try:
        result = ProductService.view_product_detail(id)
        return jsonify (result), 201
    except ResourceNotFoundException as e:
        return jsonify({"error":e.message}), e.status_code
    except Exception as e:
        return jsonify({"error":str(e)}), 400


@product_bp.route("", methods=["POST"])
def add_product():
    data = request.json
    if not data or "id" not in data or "name" not in data or "price" not in data:
        return jsonify({"error":"Product details are missing"}), 400
    try:
        result = ProductService.add_product(data)
        return jsonify (result), 201
     
     
    except Exception as e:
        return jsonify({"error":str(e)}), 400
         

@product_bp.route("/<int:id>", methods=["PUT","PATCH"])
def update_product(id):
    data = request.json
    if not id or not("name" in data or "price" in data):
        return jsonify({"error":"Missing product details"}),400
    try:
        result = ProductService.update_product(id, data)
        return jsonify (result), 200
    except ResourceNotFoundException as e:
        return jsonify({"error":e.message}), e.status_code
    except Exception as e:
        return jsonify({"error":str(e)}), 400
         



@product_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    if not id:
        return jsonify({"error":"Missing Product Id"}),400
    try:
        result = ProductService.delete_product(id)
        return jsonify (result), 200
    except ResourceNotFoundException as e:
        return jsonify({"error":e.message}), e.status_code
    except Exception as e:
        return jsonify({"error":"Unexpected Error"}), 400


