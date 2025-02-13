from src.models.order_model import orders_collection, Order

class OrderService:
    @staticmethod
    def create_order(customer_name, items, total_price):  
        #Crea una nueva orden y la almacena en MongoDB.#
        order = Order(customer_name, items, total_price)
        order_id = orders_collection.insert_one(order.to_dict()).inserted_id
        return str(order_id)  # Retornar el ID de la orden creada
