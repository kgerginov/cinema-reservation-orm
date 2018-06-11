from hashlib import pbkdf2_hmac
from prettytable import PrettyTable


def hash_pass(username, password):
    hashed_pass = pbkdf2_hmac('sha256', password.encode(), username.encode(), 10000).hex()
    return hashed_pass


def pretty_print_movies(movies):
    table = PrettyTable()
    table.field_names = ["Id", "Name", "Rating"]
    for m in movies:
        table.add_row([m.id, m.name, m.rating])
    print(table)


def pretty_print_movie_projections(projections):
    table = PrettyTable()
    table.field_names = ["Id", "Movie", "Date", "Time", "Type"]
    for pr in projections:
        table.add_row([pr.id, pr.movie_id, pr.date, pr.time, pr.type])
    print(table)


def print_matrix_hall(matrix):
    table = PrettyTable()
    table.field_names = ["-"] + list(range(1, len(matrix) + 1))
    i = 1
    for line in matrix:
        table.add_row([i] + line)
        i += 1
    print(table)


def cast_to_int(num):
    try:
        return int(num)
    except Exception:
        raise ValueError('Invalid number?')



