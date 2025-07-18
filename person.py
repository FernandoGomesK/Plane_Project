from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def be_assigned(self, flight_id, seat_id = None):
        pass

class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def be_assigned(self, flight_id, seat_id):
        print(f"Passenger {self.name} is assigned to flight {flight_id} and seat {seat_id}")
        

class FlightCrew(Person):
    def __init__(self, name: str, role: str):
        super().__init__(name)
        self._role = role 
        
    @property
    def role(self):
        return self._role
    
    def be_assigned(self, flight_id, seat_id = None):
        print(f"Flight crew member {self.name} {self.role} is assigned to flight {flight_id}")
        