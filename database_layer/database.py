from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, Float, Boolean,
                        Date, Time, CheckConstraint, ForeignKey)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from settings import DB_NAME

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rating = Column(Float, CheckConstraint('rating>0'), CheckConstraint('rating<10'))


class Projection(Base):
    __tablename__ = 'projection'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    type = Column(String(3))
    date = Column(Date)
    time = Column(Time)
    movie = relationship(Movie, backref='projection')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    logged_in = Column(Boolean, default=False)


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    projection_id = Column(Integer, ForeignKey('projection.id'))
    row = Column(Integer)
    col = Column(Integer)
    projection = relationship(Projection, backref='reservation')
    user = relationship(User, backref='reservation')


engine = create_engine('postgresql://postgres@localhost:5432/{}'.format(DB_NAME))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
#
# s = Session()
#
# star = s.query(Movie).filter(Movie.name == 'Star Wars')

