import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(80), unique=False, nullable=False)


class Characters(Base):
    __tablename__ = 'characters'

    id_characters = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('id.user'))
    user = relationship(User)
    gender = Column(String(25), nullable = False)
    birth_year = Column(String(25), nullable = False)


class Likes(Base):
    __tablename__ = 'likes'

    id_likes = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, nullable=False)
    user = relationship(User)
    
class Vehicles(Base):
    __tablename__ = 'vehicles'

    id_vehicles = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    user = relationship(User)
    post = relationship(Post)

class Planets(Base):
    __tablename__ = 'planets'

    id_planets = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    name = Column(String(25), nullable = False)
    population = Column(Integer, nullable=False)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
