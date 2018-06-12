from database_layer.database import (Movie,
                                     Projection)
from database_layer.database import Session
from utills.validator import CinemaValidator


class MovieController:
    session = Session()
    validator = CinemaValidator()

    def add_new_movie(self, movie_name, movie_rating):
        self.validator.validate_new_movie(movie_name, movie_rating)
        self.session.add(Movie(name=movie_name, rating=movie_rating))
        self.session.commit()

    def add_movie_projection(self, movie_id, movie_type, movie_date, movie_time):
        self.validator.validate_projection(movie_id, movie_date, movie_time)
        movie = self.session.query(Movie).filter(Movie.id == movie_id).one()
        movie.projection.append(Projection(
            movie_id=movie_id, type=movie_type,
            date=movie_date, time=movie_time
        ))
        self.session.commit()

    def list_movies(self):
        return self.session.query(Movie).\
            order_by(Movie.rating.desc()).all()

    def list_movie_projections_ordered_by_date(self, id):
        self.validator.validate_movie_id(id)
        return self.session.query(Projection).\
            filter(Projection.movie_id == id).\
            order_by(Projection.date).all()

    def list_movie_projections_by_date(self, id, date):
        self.validator.validate_movie_id(id)
        self.validator.validate_date_format(date)
        return self.session.query(Projection).\
            filter(Projection.movie_id == id).\
            filter(Projection.date == date).\
            order_by(Projection.time).all()

    def show_movie_projections(self, id, date=None):
        if date:
            return self.list_movie_projections_by_date(id, date)
        else:
            return self.list_movie_projections_ordered_by_date(id)


if __name__ == '__main__':
   m = MovieController()
   m.add_movie_projection(1, '5g', '2018-05-26', '20:51')