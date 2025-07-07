import random
from seat import Seat
from person import Person, Passenger
import uuid

class Flight:
    def __init__(self,total_seats: str):
        self.flight_id = str(uuid.uuid4())[:4]
        self.total_seats = int(total_seats)
        self.pilot = None
        self.copilot = None
        self.seats = [Seat() for x in range(1, total_seats + 1)]

    def show_seats(self):
        for s in self.seats:
            print(f"flight id: {self.flight_id}")
            s.show_seat_info()
            
    def assign_crew(self, pilot: Person, copilot: Person):
        self.pilot = pilot
        self.copilot = copilot
        
    def assign_passenger(self, passenger: Passenger):
        for s in self.seats:
            if not s.is_occupied():
                s.passenger = passenger
                passenger.be_assigned(self.flight_id, s.seat_id)
                return True
        print(f"flight {self.flight_id} is full")
        return False
    
    def count_occupied_seats(self):
        return sum(1 for seat in self.seats if seat.is_occupied())


    def aleatory_passenger_choose(self):
        occupied_seat_list = [seat for seat in self.seats if seat.is_occupied()]
        sample_size = min(10, len(occupied_seat_list))
        if sample_size > 0:
            return random.sample(occupied_seat_list, sample_size)
        return []
                
    def display_manifest(self):
        """Mostra todos os assentos e quem está neles."""
        print("-" * 30)
        print(f" flight manifest: {self.flight_id}")
        print(f"pilot: {self.pilot.name} | copilot: {self.copilot.name}")
        print("-" * 30)
        print(f" total seats: {self.total_seats} | occupied seats: {self.count_occupied_seats()}")
        
        passenger_sample = self.aleatory_passenger_choose()
        if passenger_sample:
            for seat in passenger_sample:
                seat.show_seat_info()
        print("-" * 30)
   