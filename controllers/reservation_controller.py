from database_layer.database import Session
from database_layer.database import (User,
                                     Reservation)
from utills.validator import CinemaValidator


class ReservationController:
    session = Session()
    validator = CinemaValidator()

    def make_new_reservation(self, user_id, proj_id, row, col):
        self.validator.validate_reservation(proj_id, row, col)
        user = self.session.query(User).\
            filter(User.id == user_id).one()
        user.reservation.append(Reservation(user_id=user_id, projection_id=proj_id,
                                            row=row, col=col))

    def get_taken_seats_for_projection(self, proj_id):
        return self.session.query(Reservation.row, Reservation.col).\
            filter(Reservation.projection_id == proj_id).all()

    def finalize_reservation(self):
        self.session.commit()


if __name__ == '__main__':
    r = ReservationController()
