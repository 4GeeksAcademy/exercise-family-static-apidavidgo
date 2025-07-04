"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200


@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json
    print(new_member)
    jhon= {
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]},
    
    jackson_family.add_member("primo_paco", "tio_pedro", "abuela_chari")
    return jsonify({"Todo ok,": "Usuario creado"})


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    eliminar_familiar = jackson_family.delete_member(member_id)

    if not eliminar_familiar:
        return jsonify({"msg": "Ese familiar no existe"}), 400

    return jsonify({"done": "Familiar borrado"}), 200

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_family_member(member_id):
    new_member = request.json  
    updated_member = jackson_family.update_member(member_id, "new_member")
    if not updated_member:
        return jsonify({"msg":"No se ha encontrado al miembro"}), 400
    return jsonify({"done": "Familiar actualizado"}), 200

@app.route('/member/int:member_id>', methods=['GET'])
def get_one_member(member_id):
    founded_member = jackson_family.get_member(member_id)
    if not founded_member:
        return jsonify({"msg":"Miembro no encontrado"}), 400
    return jsonify({"done":"Miembro encontrado"}), 200





# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
