from controllers.movie_controller import MovieController
from controllers.user_controller import UserController
from controllers.reservation_controller import ReservationController

m = MovieController()
u = UserController()
r = ReservationController()

def pop():
    # m.add_new_movie(movie_name='LODR', movie_rating=9)
    # m.add_new_movie(movie_name='bbee', movie_rating=3)
    # m.add_new_movie(movie_name='star', movie_rating=2)
    # m.add_new_movie(movie_name='wars', movie_rating=5)
    # m.add_new_movie(movie_name='13', movie_rating=5)

    # u.create_new_user(user_name='Ivan', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan2', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan3', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan4', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan5', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan6', password='Bahmu123@')
    # u.create_new_user(user_name='Ivan7', password='Bahmu123@')
    r.make_new_reservation(1, 2, 9, 9)
    r.make_new_reservation(1, 2, 9, 8)
    r.make_new_reservation(1, 2, 9, 7)
    r.make_new_reservation(1, 2, 9, 10)

    # p.create_new_projection(movie_id=1, type_='3D', date='2018-02-12', time='12:30:00')
    # p.create_new_projection(movie_id=2, type_='2D', date='2018-05-02', time='12:30:00')
    # p.create_new_projection(movie_id=3, type_='4D', date='2018-06-22', time='12:30:00')
    # p.create_new_projection(movie_id=4, type_='5D', date='2018-07-15', time='12:30:00')



pop()