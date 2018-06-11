from ast import literal_eval
from interface.movie_interface import MovieInterface
from interface.user_interface import UserInterface
from models.validator import CinemaValidator


class Interface:
    user_interface = UserInterface()
    movie_interface = MovieInterface()
    validator = CinemaValidator()

    def __init__(self):
        self.user_id = None

    def start(self):
        while True:
            try:
                command = input('Enter command.\n>>> ')
                self.get_command_action(command)
            except ValueError as e:
                print(e)

    def commands(self):
        print('[1] - show movies\n'
              '[2] - show movie projection <movie id> <date> - date optional\n'
              '[3] - make reservation\n'
              '[4] - help')

    def get_command_action(self, command):
        if command == 'show movies':
            self.movie_interface.show_movies()
        elif command.startswith('show movie projection'):
            args = command.split('show movie projection ')
            args = args[1].split(' ')
            if len(args) > 2:
                raise ValueError('Too many arguments. Did you press SPACE?')
            self.movie_interface.show_movie_projections(*args)

        elif command == 'make reservation':
            if not self.user_id:
                self.user_id = self.user_interface.reg_or_log()
            self.reserve()
        elif command == 'help':
            self.commands()

        else:
            raise ValueError('Unknown command!')

    def __get_seats(self):
        num_of_seats = int(input('Number of seats:\n>>> '))
        print('Free seats are marked with a dot. Taken seats with a "X".\n'
              'Choose seat by the matrix. For example first seat '
              'to the left will be (1, 1). You can choose for as many tickets as u have\n'
              'For example 2 tickets. You choose (1, 2), (4, 5). 2 seats chosen!')
        count = 0
        chosen_seats = []
        while num_of_seats != count:
            try:
                seat = input('Choose seat:\n>>> ')
                seat = literal_eval(seat)
                # print(len(seat))
                if type(seat) is not tuple:
                    raise ValueError('Invalid choice. Choose as shown!')
            except ValueError as e:
                print(e)
            else:
                chosen_seats.append(seat)
                count += 1
        return chosen_seats

    def reserve(self):
        movie_id = self.movie_interface.choose_movie()
        proj_id = self.movie_interface.choose_movie_projection(movie_id)
        self.movie_interface.show_room_matrix_for_projection(proj_id)
        seats = self.__get_seats()
        for seat in seats:
            self.user_interface.make_reservation(self.user_id, proj_id, seat[0], seat[1])

        # print(seat)
        # self.user_interface.make_reservation(self.user_id, proj_id, row, col)


if __name__ == '__main__':
    i = Interface()
    print(i.start())
