
from person import Passenger

class Seat:
    def __init__(self, seat_id: int):
        self._seat_id = seat_id
        self._passenger = None
        
    @property
    def seat_id(self):
        return self._seat_id
    
    @property
    def passenger(self):
        return self._passenger
    @property
    def is_occupied(self) -> bool:
        return self._passenger is not None
    
    def assign(self, passenger: Passenger):
        if not self.is_occupied:
            self._passenger = passenger
            return True
        return False
    
    def show_seat_info(self):
        if self.is_occupied:
            print(f" seat id: {self.seat_id} is occupied by {self.passenger.name}")
        else:
            print(f" seat id: {self.seat_id} is not occupied")
     
        