from enum import Enum

class AirplaneModel(Enum):
    BOEING_747 = ("Boeing 747", 250)
    AIRBUS_A318 = ("Airbus A318", 150)
    
    
    def __init__(self, model_name, seat_capacity):
        self.model_name = model_name
        self.seat_capacity = seat_capacity
        