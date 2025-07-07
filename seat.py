import uuid

class Seat:
    def __init__(self):
        self.seat_id = str(uuid.uuid4())[:4]
        self.passenger = None
        
    def is_occupied(self):
        return self.passenger is not None
    def show_seat_info(self):
        if self.is_occupied():
            print(f" seat id: {self.seat_id} is occupied by {self.passenger.name}")
        else:
            print(f" seat id: {self.seat_id} is not occupied")
     
        