import uuid

class Seat:
    def __init__(self):
        self.seat_id = str(uuid.uuid4())[:4]
        self.passenger = []
        
    def show_seats(self):
        print(f" seat id: {self.seat_id}")
        