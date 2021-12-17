import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    surname = Column(String(250))
    email = Column(String(60))
    password = Column(String(30), nullable = False)
    subscription_date = Column(String(60))
   
class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(30))

class Character(Base):
    __tablename__ = 'character'
    char_id = Column(Integer, primary_key=True)
    char_name = Column(String(200))
    char_planet = Column(String(30))
    planet = relationship(Planet)
    
class Favs(Base):
    __tablename__ = 'favs'
    user_name = Column(String(250), nullable =  False)
    fav_planet = relationship(Planet)
    fav_character = relationship(Character)
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')