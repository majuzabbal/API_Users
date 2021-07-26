from flask import Blueprint
from flask import request, jsonify
from flask_cors import cross_origin
import json

from Models.users import User

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def create_user():
    record = json.loads(request.data)
    print(request.args.get('nome'))
    user = User(cpf=record['cpf'],
                nome=record['nome'],
                email=record['email'],
                data_nascimento=record['data_nascimento'],
                endereco=record['endereco'])
    user.save()
    return jsonify(user.to_json()), 201


@users_blueprint.route('/users/<cpf>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index_by_cpf(cpf):
    user = User.objects(cpf=cpf).first()

    if not cpf:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())


@users_blueprint.route('/users', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def index():
    users = User.objects()

    print(users)
    response = []

    for user in users:
        response.append(user.to_json())
    if not users:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(response)


@users_blueprint.route('/users/<cpf>', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def delete_user(cpf):
    user = User.objects(cpf=cpf).first()

    if not user:
        return jsonify({'error': 'data not found'}), 404
    else:
        try:
            user.delete()
            return jsonify(), 204
        except Exception as e:
            print(e)
    return jsonify(), 204
