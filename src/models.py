import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250))
    surname = Column(String(250))
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(30), nullable = False)
    subscription_date = Column(String(60))
    
    fav_planet = relationship('Favorite planet', back_populates='FavPlanet.favPl_id', primaryjoin='User.id==FavPlanet.favPl_id', lazy='dynamic')
    fav_char = relationship('Favorite character', back_populates='FavChar.favCh_id', primaryjoin='User.id==FavChar.favCh_id', lazy='dynamic')

class Planet(Base):
    __tablename__ = 'Planet'
    planet_id = Column(Integer, primary_key=True, autoincrement=True)
    planet_name = Column(String(30), unique=True)

class Character(Base):
    __tablename__ = 'Character'
    char_id = Column(Integer, primary_key=True, autoincrement=True)
    char_name = Column(String(200))
    char_surName = Column(String(200))
    char_planet = Column(Integer, ForeignKey(Planet.planet_id))
    planet_now = Column(String(30))    
    
class FavChar(Base):
    __tablename__ = 'Favorite character'
    favChr_id = Column(Integer, primary_key=True, autoincrement=True)
    user_favChr_id = Column(Integer, ForeignKey(User.id))
    fav_character = Column(Integer, ForeignKey(Character.char_id))    
    
class FavPlanet(Base):
    __tablename__ = 'Favorite planet'
    favPl_id = Column(Integer, primary_key=True, autoincrement=True)
    user_favPl_id = Column(Integer, ForeignKey(User.id))
    fav_planet = Column(Integer, ForeignKey(Planet.planet_id))
    
render_er(Base, 'diagram.png')