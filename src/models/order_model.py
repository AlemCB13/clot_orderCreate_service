from pymongo import MongoClient
from datetime import datetime
import os

# Obtener la URI de conexión desde la variable de entorno
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/clot_orders")

# Conectar a MongoDB
client = MongoClient(mongo_uri)
db = client.get_database()
orders_collection = db.orders  # Nombre de la colección donde se guardarán las órdenes

class Order:
    def __init__(self, customer_name, items, total_price):
        self.customer_name = customer_name
        self.items = items  # Lista de productos comprados
        self.total_price = total_price
        self.created_at = datetime.utcnow()

    def to_dict(self):
    #Convierte la orden en un diccionario listo para ser insertado en MongoDB.#
        return {
            "customer_name": self.customer_name,
            "items": self.items,
            "total_price": self.total_price,
            "created_at": self.created_at
        }
