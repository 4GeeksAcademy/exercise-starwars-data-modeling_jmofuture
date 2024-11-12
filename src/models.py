import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
#from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


favorites_association = Table(
    'favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planets.id'), nullable=True),
    Column('character_id', Integer, ForeignKey('characters.id'), nullable=True)
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    

    favorites = relationship('Favorite', secondary=favorites_association, back_populates='user')


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    

    favorites = relationship('Favorite', secondary=favorites_association, back_populates='planet')


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(50))
    mass = Column(String(50))
    

    favorites = relationship('Favorite', secondary=favorites_association, back_populates='character')


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')


try:
    render_er(Base, 'diagram.png')
    print("Diagrama generado")
except Exception as e:
    print("Error:", e)