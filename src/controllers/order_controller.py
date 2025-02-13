from flask import Blueprint, request, jsonify
from services.order_service import OrderService

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/orders", methods=["POST"])
def create_order():

    #Endpoint para crear una nueva orden.#

    try:
        data = request.get_json()
        if not data or "customer_name" not in data or "items" not in data or "total_price" not in data:
            return jsonify({"error": "Faltan campos requeridos"}), 400

        order_id = OrderService.create_order(
            customer_name=data["customer_name"],
            items=data["items"],
            total_price=data["total_price"]
        )

        return jsonify({"message": "Orden creada exitosamente", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
