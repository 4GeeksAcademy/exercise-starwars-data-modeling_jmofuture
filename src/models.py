import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime
from sqlalchemy.orm import relationship, declarative_base

from eralchemy2 import render_er
from datetime import datetime

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
    subscription_date = Column(DateTime, default=datetime.now())

    favorite_planets = relationship('Planet', secondary=favorites_association, back_populates='favorited_by')
    favorite_characters = relationship('Character', secondary=favorites_association, back_populates='favorited_by')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    

    favorited_by = relationship('User', secondary=favorites_association, back_populates='favorite_planets')

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(50))
    mass = Column(String(50))
    

    favorited_by = relationship('User', secondary=favorites_association, back_populates='favorite_characters')


try:
    render_er(Base, 'diagram.png')
    print("Diagrama generado")
except Exception as e:
    print("Error:", e)
