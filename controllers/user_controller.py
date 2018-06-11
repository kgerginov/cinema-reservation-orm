from sqlalchemy.orm import joinedload
from database_layer.database import Session
from database_layer.database import (User,
                                     Reservation)
from models.validator import CinemaValidator
from models.utills import hash_pass


class UserController:
    session = Session()
    validator = CinemaValidator()

    def create_new_user(self, username, password):
        self.validator.check_if_user_exists(username)
        self.validator.validate_password(password)
        self.session.add(User(username=username,
                              password=hash_pass(username, password)))
        self.session.commit()

    def get_user_id_by_username(self, username):
        # self.validator.check_if_user_exists(username)
        return self.session.query(User.id).\
            filter(User.username == username).one()[0]

    def log_user_in(self, username, password):
        self.validator.check_user_password(username, password)
        user = self.session.query(User).\
            filter(User.username == username).one()
        user.logged_in = True
        self.session.commit()

    def log_user_out(self, id_):
        user = self.session.query(User).\
            filter(User.id == id_).one()
        user.logged_in = False
        self.session.commit()

    def log_all_users_out(self):
        self.session.query(User).update({'logged_in': False})
        self.session.commit()

    def get_user_reservations(self, id_):
        return self.session.query(Reservation).\
            filter(Reservation.user == id_).all()





if __name__ == '__main__':
    u = UserController()
    print(u.get_user_id_by_username('asdasd'))