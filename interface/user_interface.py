from controllers.reservation_controller import ReservationController
from controllers.user_controller import UserController
from utills.exceptions import (UserAlreadyExists)
from utills.validator import CinemaValidator


# import getpass


class UserInterface:
    user_controller = UserController()
    reservation_controller = ReservationController()
    validator = CinemaValidator()

    def reg_or_log(self):
        while True:
            print('You need to log in or register first!\n'
                  'Enter what u want to do!\n1. '
                  'Register\n2. log in?')
            choice = input('>>> ')
            try:
                return self.__log_or_register(choice)
            except ValueError as e:
                print(e)
                # self.__log_or_register(choice)
            except UserAlreadyExists as e:
                print(e)
                # self.__log_or_register(choice)

    def register(self):
        username = self.__get_username()
        password = self.__get_register_password()
        self.user_controller.create_new_user(username, password)
        print('Successful registration!')
        return self.user_controller.get_user_id_by_username(username)

    def log_in(self):
        username = self.__get_username()
        password = self.__get_login_password()
        self.user_controller.log_user_in(username, password)
        print('Successful login!')
        return self.user_controller.get_user_id_by_username(username)

    def make_reservation(self, user_id, proj_id, row, col):
        self.reservation_controller.make_new_reservation(user_id, proj_id, row, col)

    def finalize_reservation(self):
        self.reservation_controller.finalize_reservation()

    def __log_or_register(self, choice):
        if choice == '1':
            return self.register()

        elif choice == '2':
            return self.log_in()

        else:
            print('Choice not valid!')

    def __get_username(self):
        while True:
            try:
                username = input('Enter username:\n>>> ')
                self.validator.validate_username(username)
            except ValueError as e:
                print(e)
            else:
                return username

    @staticmethod
    def __get_login_password():
        password = input('Enter password:\n>>> ')
        return password

    def __get_register_password(self):
        while True:
            try:
                pass_1 = input('Enter password:\n >>> ')
                self.validator.validate_password(pass_1)
                pass_2 = input('Confirm password:\n >>> ')
                if pass_1 != pass_2:
                    raise ValueError('Different passwords!')
            except ValueError as e:
                print(e)
            else:
                return pass_1


if __name__ == '__main__':
    i = UserInterface()
