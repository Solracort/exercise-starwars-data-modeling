import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname  = Column(String(250), nullable=False)
    email     = Column(String(250), nullable=False)
    
    relcomment  = relationship('Comment', backref='comment', lazy=True)
    relpost  = relationship('Post', backref='post', lazy=True)
    relfollower = relationship('Follower', backref='user', lazy=True)
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    idfollower   = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id   = Column(Integer, ForeignKey('user.id'))
    
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    idcomment = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id   = Column(Integer, ForeignKey('post.idpost'))    
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    idpost = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    relcomment = relationship('Comment', backref='comment', lazy=True)   
    relmedia = relationship('Media' , backref='media', lazy=True)   
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    idmedia = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url  = Column(String(250), nullable=False)      
    post_id = Column(Integer, ForeignKey('post.idpost')) 
    
    
def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
