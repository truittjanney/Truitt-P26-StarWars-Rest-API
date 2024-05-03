"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicle, User_Character_Favorite, User_Planet_Favorite, User_Vehicle_Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# User App Routes

@app.route('/users', methods=['GET'])
def fetch_user():

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

# @app.route('/users/favorites', methods=['GET'])
# def fetch_user_favorites():

#     user_favorites = (className).query.all()
#     all_characters = list(map(lambda x: x.serialize(), characters))

#     return jsonify(all_characters), 200

# Character App Routes

@app.route('/characters', methods=['GET'])
def fetch_characters():

    characters = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), characters))

    return jsonify(all_characters), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def fetch_character_info(character_id):

    character = db.get_or_404(Character, character_id)

    response_body = {
        "msg": "Character info received!"
    }

    return jsonify(character.serialize()), 200

@app.route('/user/<int:user_id>/favorite/characters/<int:characters_id>', methods=['POST'])
def add_character_favorite(user_id, character_id):
    favorite_character = User_Character_Favorite(user_id = user_id, character_id = character_id)
    
    db.session.add(favorite_character)
    db.session.commit()

    return jsonify("Character favorited!"), 200

@app.route('/user/<int:user_id>/favorite/characters/<int:characters_id>', methods=['DELETE'])
def delete_character_favorite(user_id, character_id):
    favorite_character = User_Character_Favorite.query.filter_by(user_id = user_id, character_id = character_id).first()
    db.session.delete(favorite_character)
    response_body = {
        "msg": "Character favorite deleted!"
    }

    return jsonify("Character favorite deleted!"), 200

# Planets App Routes

@app.route('/planets', methods=['GET'])
def fetch_planets():

    planets = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planets))

    return jsonify(all_planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def fetch_planet_info(planet_id):

    planet = db.get_or_404(Planet, planet_id)

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(planet.serialize()), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['POST'])
def add_planet_favorite(user_id, planet_id):

    favorite_planet = User_Planet_Favorite(user_id = user_id, planet_id = planet_id)
    
    db.session.add(favorite_planet)
    db.session.commit()

    return jsonify("Planet favorited!"), 200

@app.route('/user/<int:user_id>/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(user_id, planet_id):

    favorite_planet = User_Planet_Favorite.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    db.session.delete(favorite_planet)
    response_body = {
        "msg": "Planet favorite deleted!"
    }

    return jsonify("Planet favorite deleted!"), 200

# Vehicle App Routes

@app.route('/vehicles', methods=['GET'])
def fetch_vehicles():

    vehicles = Vehicle.query.all()
    all_vehicles = list(map(lambda x: x.serialize(), vehicles))

    return jsonify(all_vehicles), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def fetch_vehicle_info(vehicle_id):

    vehicle = db.get_or_404(Vehicle, vehicle_id)

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(vehicle.serialize()), 200

@app.route('/user/<int:user_id>/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_vehicle_favorite(user_id, vehicle_id):

    favorite_vehicle = User_Vehicle_Favorite(user_id = user_id, vehicle_id = vehicle_id)
    
    db.session.add(favorite_vehicle)
    db.session.commit()

    return jsonify("Vehicle favorited!"), 200

@app.route('/user/<int:user_id>/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle_favorite(user_id, vehicle_id):

    favorite_vehicle = User_Vehicle_Favorite.query.filter_by(user_id = user_id, vehicle_id = vehicle_id).first()
    db.session.delete(favorite_vehicle)
    response_body = {
        "msg": "Vehicle favorite deleted!"
    }

    return jsonify("Vehicle favorite deleted!"), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
