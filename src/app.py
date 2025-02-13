from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from controllers.order_controller import order_bp


# Cargar variables de entorno
load_dotenv()

# Verificar si la variable de entorno está definida
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("Error: La variable de entorno MONGO_URI no está definida.")

app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient(mongo_uri)
db = client["clot_orders"]  # Especificar la base de datos explícitamente

# Registrar las rutas desde el controlador
app.register_blueprint(order_bp, url_prefix="/api")

@app.route("/", methods=["GET"])
def home():
    return {"message": "Clot Order Create Service is running!"}, 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
