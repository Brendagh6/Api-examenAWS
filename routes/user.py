from flask import Blueprint, jsonify, request
from controllers.userController import (
    get_all_users,
    create_user,
    login_user,
    get_user,
    update_user,
    delete_user,
)

user_bp = Blueprint("usuarios", __name__)


# Obtener todos los usuarios
@user_bp.route("/", methods=["GET"])
def index():
    """
    Obtener todos los usuarios
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuarios
        schema:
          type: array
          items:
            type: object
    """
    user = get_all_users()
    return jsonify(user)


# Obtener un usuario específico
@user_bp.route("/<int:id_usuario>", methods=["GET"])
def get_one_user(id_usuario):
    """
    Obtener un usuario por ID
    ---
    tags:
      - Usuarios
    parameters:
      - name: id_usuario
        in: path
        type: integer
        required: true
        description: ID del usuario a consultar
    responses:
      200:
        description: Usuario encontrado
      404:
        description: Usuario no encontrado
    """
    user = get_user(id_usuario)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Crear un nuevo usuario
@user_bp.route("/", methods=["POST"])
def user_store():
    """
    Crear un nuevo usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: usuario
        required: true
        schema:
          type: object
          required:
            - nombre
            - correo
            - passw
          properties:
            nombre:
              type: string
              description: Nombre del usuario
            correo:
              type: string
              description: Correo del usuario
            passw:
              type: string
              description: Contraseña del usuario
    responses:
      200:
        description: Usuario creado exitosamente
    """
    data = request.get_json()
    nombre = data.get("nombre")
    correo = data.get("correo")
    passw = data.get("passw")
    new_user = create_user(nombre, correo, passw)
    return jsonify(new_user)


# Eliminar un usuario
@user_bp.route("/<int:id_usuario>", methods=["DELETE"])
def user_destroy(id_usuario):
    """
    Eliminar un usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: id_usuario
        in: path
        type: integer
        required: true
        description: ID del usuario a eliminar
    responses:
      200:
        description: Usuario eliminado
      404:
        description: Usuario no encontrado
    """
    user = delete_user(id_usuario)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Actualizar un usuario
@user_bp.route("/<int:id_usuario>", methods=["PUT"])
def user_update(id_usuario):
    """
    Actualizar un usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - name: id_usuario
        in: path
        type: integer
        required: true
        description: ID del usuario a actualizar
      - in: body
        name: usuario
        required: true
        schema:
          type: object
          required:
            - nombre
            - correo
            - passw
          properties:
            nombre:
              type: string
            correo:
              type: string
            passw:
              type: string
    responses:
      200:
        description: Usuario actualizado
      404:
        description: Usuario no encontrado
    """
    data = request.get_json()
    nombre = data.get("nombre")
    correo = data.get("correo")
    passw = data.get("passw")
    user = update_user(id_usuario, nombre, correo, passw)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


# Login
@user_bp.route("/login", methods=["POST"])
def login():
    """
    Iniciar sesión
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: credenciales
        required: true
        schema:
          type: object
          required:
            - correo
            - passw
          properties:
            correo:
              type: string
              description: Correo del usuario
            passw:
              type: string
              description: Contraseña del usuario
    responses:
      200:
        description: Inicio de sesión exitoso
      401:
        description: Credenciales inválidas
    """
    data = request.get_json()
    return login_user(data["correo"], data["passw"])
