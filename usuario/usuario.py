from flask import Blueprint, request, jsonify
from models import Usuario
from extensions import db

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for usuario in usuarios:
        resultado.append({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido
        })
    return jsonify(resultado), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is not None:
        return jsonify({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido
        }), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

# Ruta para crear un nuevo usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(id=data['id'], nombre=data['nombre'], apellido=data['apellido'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado con éxito', 'id': nuevo_usuario.id}), 201

# Ruta para actualizar un usuario por ID
@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is not None:
        data = request.get_json()
        usuario.nombre = data['nombre']
        usuario.apellido = data['apellido']
        db.session.commit()
        return jsonify({'mensaje': 'Usuario actualizado con éxito'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404

# Ruta para eliminar un usuario por ID
@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is not None:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'mensaje': 'Usuario eliminado con éxito'}), 200
    return jsonify({'mensaje': 'Usuario no encontrado'}), 404