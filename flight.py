from seat import Seat
from person import Person, Passenger
import uuid

class Flight:
    def __init__(self,total_seats: str):
        self.flight_id = str(uuid.uuid4())[:4]
        self.total_seats = int(total_seats)
        self.seats = [Seat() for x in range(1, total_seats + 1)]

    def show_seats(self):
        for s in self.seats:
            print(f"flight id: {self.flight_id}")
            s.show_seat_info()
            
    def assign_passenger(self, passenger: Passenger):
        for s in self.seats:
            if not s.is_occupied():
                s.passenger = passenger
                passenger.be_assigned(self.flight_id, s.seat_id)
                return True
        print(f"flight {self.flight_id} is full")
        return False

    def display_manifest(self):
        """Mostra todos os assentos e quem está neles."""
        print("-" * 30)
        print(f" flight manifest: {self.flight_id}")
        for seat in self.seats:
            seat.show_seat_info()
        print("-" * 30)
   