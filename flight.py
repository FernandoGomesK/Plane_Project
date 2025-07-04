from seat import Seat
import uuid

class Flight:
    def __init__(self,total_seats: str):
        self.flight_id = str(uuid.uuid4())[:4]
        self.total_seats = int(total_seats)
        self.seats = [Seat() for x in range(int(total_seats))]

    def show_seats(self):
        for s in self.seats:
            s.show_seats()
            
    def show_id(self):
        print(f"flight id: {self.flight_id}")
        print(f"total seats: {self.total_seats}")