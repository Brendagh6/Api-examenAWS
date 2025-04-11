from config import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    passw = db.Column(db.String(200), nullable=False)
   
    
    def __init__(self, nombre,correo, passw):
        self.nombre = nombre
        self.correo = correo
        self.passw = generate_password_hash(passw)




    def check_password (self, passw):
            return check_password_hash(self.passw, passw); 
    
    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "passw": self.passw,
        }
    