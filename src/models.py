import os
import sys
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table, DECIMAL, BigInteger  
from sqlalchemy.orm import relationship, declarative_base, backref  # type: ignore
from sqlalchemy import create_engine  
from eralchemy2 import render_er  

Base = declarative_base()

film_characters = Table(
    'film_characters',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('people.id'), primary_key=True)
)

film_planets = Table(
    'film_planets',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planets.id'), primary_key=True)
)

film_starships = Table(
    'film_starships',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('starship_id', Integer, ForeignKey('starships.id'), primary_key=True)
)

film_vehicles = Table(
    'film_vehicles',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'), primary_key=True)
)

film_species = Table(
    'film_species',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('species_id', Integer, ForeignKey('species.id'), primary_key=True)
)

species_people = Table(
    'species_people',
    Base.metadata,
    Column('species_id', Integer, ForeignKey('species.id'), primary_key=True),
    Column('person_id', Integer, ForeignKey('people.id'), primary_key=True)
)

# TABLAS

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(BigInteger)
    climate = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(Integer)
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    # RELACIONES
    residents = relationship("Person", backref="homeworld_planet")
    species = relationship("Species", backref="homeworld_planet")


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(20))
    gender = Column(String(20))
    homeworld = Column(Integer, ForeignKey('planets.id', ondelete='SET NULL'))
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    #
    films = relationship("Film", secondary=film_characters, backref="characters")
    species = relationship("Species", secondary=species_people, backref="people")


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    model = Column(String(255))
    vehicle_class = Column(String(100))
    manufacturer = Column(String(255))
    cost_in_credits = Column(BigInteger)
    length = Column(DECIMAL(10, 2))
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(BigInteger)
    consumables = Column(String(50))
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    films = relationship("Film", secondary=film_vehicles, backref="vehicles")


class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    model = Column(String(255))
    starship_class = Column(String(100))
    manufacturer = Column(String(255))
    cost_in_credits = Column(BigInteger)
    length = Column(DECIMAL(10, 2))
    crew = Column(String(50))
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(DECIMAL(3, 1))
    MGLT = Column(Integer)
    cargo_capacity = Column(BigInteger)
    consumables = Column(String(50))
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    films = relationship("Film", secondary=film_starships, backref="starships")


class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    classification = Column(String(50))
    designation = Column(String(50))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    hair_colors = Column(String(255))
    skin_colors = Column(String(255))
    eye_colors = Column(String(255))
    homeworld = Column(Integer, ForeignKey('planets.id', ondelete='SET NULL'))
    language = Column(String(100))
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    films = relationship("Film", secondary=film_species, backref="species")


class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    episode_id = Column(Integer)
    director = Column(String(255))
    producer = Column(String(255))
    release_date = Column(DateTime)
    opening_crawl = Column(Text)
    url = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now)
    edited = Column(DateTime, default=datetime.datetime.now)

    planets = relationship("Planet", secondary=film_planets, backref="films")


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
