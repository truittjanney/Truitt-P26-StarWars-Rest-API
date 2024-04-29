from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table

db = SQLAlchemy()

tags = db.Table('tags',
    db.Column("user_id", db.Integer, db.ForeignKey("User.id"), primary_key=True),
    db.Column("character_id", db.Integer, db.ForeignKey("Character.id"), primary_key=True),
    db.Column("planet_id", db.Integer, db.ForeignKey("Planet.id"), primary_key=True),
    db.Column("vehicle_id", db.Integer, db.ForeignKey("Vehicle.id"), primary_key=True)
                )

class User_Character_Favorite(db.Model):
    __tablename__ = "User_Character_Favorite"
    user_id = db.Column(Integer, ForeignKey("User.id"), primary_key=True)
    character_id = db.Column(Integer, ForeignKey("Character.id"))

class User_Planet_Favorite(db.Model):
    __tablename__ = "User_Planet_Favorite"
    user_id = db.Column(Integer, ForeignKey("User.id"), primary_key=True)
    Planet_id = db.Column(Integer, ForeignKey("Planet.id"))

class User_Vehicle_Favorite(db.Model):
    __tablename__ = "User_Vehicle_Favorite"
    user_id = db.Column(Integer, ForeignKey("User.id"), primary_key=True)
    Vehicle_id = db.Column(Integer, ForeignKey("Vehicle.id"))

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class Character(db.Model):
    __tablename__ = "Character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    hair_color = db.Column(db.String(80), nullable=False)
    eye_color = db.Column(db.String(80), nullable=False)
    homeworld = db.Column(db.String(80), nullable=False)
    # Favorite = db.relationship("Favorite", backref="character")

class Planet(db.Model):
    __tablename__ = "Planet"
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(80), nullable=False)
    surface_water_percentage = db.Column(db.String(80), nullable=False)
    radius = db.Column(db.Float, nullable=False)
    gravity = db.Column(db.Float, nullable=False)
    # Favorite = db.relationship("Favorite", backref="planet")

class Vehicle(db.Model):
    __tablename__ = "Vehicle"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length_in_meters = db.Column(db.Float, nullable=False)
    passenger_capacity = db.Column(db.Integer, nullable=False)
    # Favorite = db.relationship("Favorite", backref="vehicle")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
# user_character_favorite = db.Table(
#     "user_character_favorite",

#     Column("user_id", ForeignKey("User.id"), primary_key=True),
#     Column("character_id", ForeignKey("Character.id"), primary_key=True),
# )

# user_planet_favorite = db.Table(
#     "user_planet_favorite",

#     Column("user_id", ForeignKey("User.id"), primary_key=True),
#     Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
# )

# user_vehicle_favorite = db.Table(
#     "user_vehicle_favorite",

#     Column("user_id", ForeignKey("User.id"), primary_key=True),
#     Column("vehicle_id", ForeignKey("Vehicle.id"), primary_key=True),
# )