from extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    roles = db.relationship('Rol', backref='usuario', lazy='dynamic')

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    aplicacion = db.Column(db.String(50))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))