from flask import Blueprint, request, jsonify
from models import Rol
from extensions import db

rol_bp = Blueprint('rol_bp', __name__)

@rol_bp.route('/roles', methods=['GET'])
def get_roles():
    roles = Rol.query.all()
    resultado = []
    for rol in roles:
        resultado.append({
            'id': rol.id,
            'aplicacion': rol.aplicacion,
            'usuario_id': rol.usuario_id
        })
    return jsonify(resultado), 200

# Ruta para obtener un rol por ID
@rol_bp.route('/roles/<int:rol_id>', methods=['GET'])
def get_one_rol(rol_id):
    rol = Rol.query.get(rol_id)
    if rol is None:
        return jsonify({'error': 'Rol no encontrado'}), 404
    return jsonify({
        'id': rol.id,
        'aplicacion': rol.aplicacion,
        'usuario_id': rol.usuario_id
    }), 200
    
# Ruta para crear un rol
@rol_bp.route('/roles', methods=['POST'])
def create_rol():
    data = request.get_json()
    nuevo_rol = Rol(aplicacion=data['aplicacion'], usuario_id=data['usuario_id'])
    db.session.add(nuevo_rol)
    db.session.commit()
    return jsonify({'message': 'Rol creado con éxito', 'id': nuevo_rol.id}), 201

# Ruta para actualizar un rol por ID
@rol_bp.route('/roles/<int:rol_id>', methods=['PUT'])
def update_rol(rol_id):
    rol = Rol.query.get(rol_id)
    if rol is None:
        return jsonify({'error': 'Rol no encontrado'}), 404

    data = request.get_json()
    rol.aplicacion = data['aplicacion']
    rol.usuario_id = data['usuario_id']

    db.session.commit()
    return jsonify({'message': 'Rol actualizado con éxito'}), 200

# Ruta para eliminar un rol por ID
@rol_bp.route('/roles/<int:rol_id>', methods=['DELETE'])
def delete_rol(rol_id):
    rol = Rol.query.get(rol_id)
    if rol is None:
        return jsonify({'error': 'Rol no encontrado'}), 404

    db.session.delete(rol)
    db.session.commit()
    return jsonify({'message': 'Rol eliminado con éxito'}), 200
