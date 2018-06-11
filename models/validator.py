import datetime
from models.utills import hash_pass
from sqlalchemy.orm.exc import NoResultFound
from settings import (MIN_USERNAME_LENGTH,
                      MIN_PASS_LENGTH,
                      SPECIAL_CHARS, MAX_ROWS, MAX_COLS)
from models.exceptions import *
from database_layer.database import Session
from database_layer.database import (User, Movie,
                                     Projection, Reservation)


class CinemaValidator:
    def __init__(self):
        self.session = Session()

    def validate_new_movie(self, name, rating):
        if rating < 0 or rating > 10:
            raise ValueError('Rating must be between 0 and 10!')
        try:
            if self.session.query(Movie).filter(Movie.name == name).one():
                raise Exception('Film already exists!')
        except NoResultFound:
            pass

    @staticmethod
    def validate_username(username):
        if len(username) < MIN_USERNAME_LENGTH:
            raise ValueError('Username must be at least {} chars!'.format(MIN_USERNAME_LENGTH))

    def _get_user_password(self, username):
        try:
            if self.check_if_user_exists(username) is None:
                raise ValueError('Username or pass incorrect!')
        except UserAlreadyExists:
            return self.session.query(User.password).\
                filter(User.username == username).one()[0]

    def check_user_password(self, username, password):
        if self._get_user_password(username) != hash_pass(username, password):
            raise ValueError('Username or password incorrect!')

    def check_if_user_exists(self, username):
        try:
            if self.session.query(User.id).filter(User.username == username).one():
                raise UserAlreadyExists('User with that username already exists!')
        except NoResultFound:
            return None

    def validate_movie_id(self, id_):
        ids = [i[0] for i in self.session.query(Movie.id)]
        if id_ not in ids:
            raise MovieDoesntExist('No such movie!')

    def validate_projection_id(self, id_, movie_id):
        ids = [i[0] for i in self.session.query(Projection.id).filter(Projection.movie_id == movie_id)]
        if id_ not in ids:
            raise ProjectionDoesntExist('No such projection!')

    def validate_projection(self, movie_id, date, time):
        self.validate_movie_id(movie_id)
        self.validate_date_format(date)
        self.validate_time_format(time)
        try:
            if self.session.query(Projection).filter(Movie.id == movie_id).\
                    filter(Projection.date == date).\
                    filter(Projection.time == time).all():
                raise ValueError('Date and time already taken. Try different time.')
        except NoResultFound:
            pass

    def validate_reservation(self, proj_id, row, col):
        if row > MAX_ROWS or col > MAX_COLS:
            raise ValueError('Invalid seat! Choose between {}, {}.'
                             .format(MAX_ROWS, MAX_COLS))
        taken_seats = self.session.query(Reservation.row, Reservation.col).\
            filter(Reservation.projection_id == proj_id).all()
        if (row, col) in taken_seats:
            raise ValueError('Seat taken!')

    # def validate_seat(self, tup):

    @staticmethod
    def validate_password(password):
        has_upper = False
        has_special = False
        has_digit = False
        if len(password) < MIN_PASS_LENGTH:
            raise ValueError('Password must be at least {} chars long!'.format(MIN_PASS_LENGTH))

        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.isdigit():
                has_digit = True
            if ch in SPECIAL_CHARS:
                has_special = True

        if not has_upper:
            raise ValueError('Password must contain a capital letter!')
        if not has_digit:
            raise ValueError('Password must contain a number!')
        if not has_special:
            raise ValueError('Password must contain a special symbol!')

    @staticmethod
    def validate_date_format(date_string):
        try:
            date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        # else:
        #     if date < datetime.datetime.now():
        #         raise ValueError('Cannot put passed dates!')

    @staticmethod
    def validate_time_format(time_string):
        try:
            datetime.datetime.strptime(time_string, '%H:%M')

        except ValueError:
            raise ValueError('Incorrect time format, should be HH:MM')



if __name__ == '__main__':
    v = CinemaValidator()
    v.validate_reservation(1, 1, 2)
