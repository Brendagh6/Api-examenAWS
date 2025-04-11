# app.py
from flask import Flask, jsonify, request
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger # Importar Swagger


# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Configuración Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'usuarios',
            "route": '/docs/usuarios.json',
            "rule_filter": lambda rule: rule.endpoint.startswith('usuarios.'),  # solo rutas del blueprint "usuarios"
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/usuarios"
}

swagger = Swagger(app, config=swagger_config) # Inicializar Swagger
CORS(app)
app.config['JWT_SECRET_KEY'] = 'Hoy desperte con ganas'
jwt = JWTManager(app)

# Configuración de la aplicación
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

# Registrar rutas
from routes.user import user_bp

app.register_blueprint(user_bp, url_prefix='/usuarios')  # Use /api as prefix

if __name__ == '__main__':
    app.run(debug=True)