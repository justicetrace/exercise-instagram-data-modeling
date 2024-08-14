import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__= 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    def serialize(self):
        return {
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    following_user_id = Column(Integer, ForeignKey("user.id"))
    followed_user_id = Column(Integer, ForeignKey("user.id"))
    def serialize(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_date = Column(String(250), nullable=False)
    post_time = Column(String(250), nullable=False)
    post_caption = Column(String(250), nullable=False)
    def serialize(self):
        return {
            'post_date': self.post_date,
            'post_tiime': self.post_time,
            'post_caption': self.post_caption,
        }
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    comment_time = Column(String(250), nullable=False)
    comment_date = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    author_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self):
        return {
            'comment_time': self.comment_time,
            'comment_date': self.comment_date,
            'post_id': self.post_id,
            'author_id': self.author_id,
            'comment_text': self.comment_text,
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
