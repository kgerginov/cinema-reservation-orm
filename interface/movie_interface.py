from controllers.movie_controller import MovieController
from controllers.reservation_controller import ReservationController
from settings import MAX_COLS, MAX_ROWS
from utills.exceptions import (MovieDoesntExist,
                               ProjectionDoesntExist)
from utills.utills import (pretty_print_movie_projections,
                           pretty_print_movies)
from utills.utills import print_matrix_hall, cast_to_int
from utills.validator import CinemaValidator


class MovieInterface:
    validator = CinemaValidator()
    movie_controller = MovieController()
    reservation_controller = ReservationController()

    def choose_movie(self):
        while True:
            try:
                self.show_movies()
                movie_id = input('Choose movie id:\n>>> ')
                self.validator.validate_movie_id(cast_to_int(movie_id))
            except MovieDoesntExist as e:
                print(e)
            except ValueError as e:
                print(e)
            else:
                return movie_id

    def choose_movie_projection(self, movie_id):
        while True:
            try:
                self.show_movie_projections(movie_id)
                projection_id = input('Choose projection id:\n>>> ')
                self.validator.validate_projection_id(cast_to_int(projection_id), movie_id)
            except ProjectionDoesntExist as e:
                print(e)
            except ValueError as e:
                print(e)
            else:
                return projection_id

    def show_movies(self):
        pretty_print_movies(self.movie_controller.list_movies())

    def show_movie_projections(self, id_, date=None):
        pretty_print_movie_projections(
            self.movie_controller.show_movie_projections(cast_to_int(id_), date))

    def show_room_matrix_for_projection(self, proj_id, seats=None):
        matrix = [['.' for _ in range(MAX_ROWS)] for _ in range(MAX_COLS)]
        taken_seats = self.reservation_controller.get_taken_seats_for_projection(proj_id)
        for seat in taken_seats:
            matrix[seat[0] - 1][seat[1] - 1] = 'x'
        if seats:
            for seat in seats:
                matrix[seat[0] - 1][seat[1] - 1] = '#'
        print_matrix_hall(matrix)
