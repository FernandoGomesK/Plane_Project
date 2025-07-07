from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def be_assigned(self, flight_id, seat_id):
        pass

class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def be_assigned(self, flight_id, seat_id):
        print(f"Passenger {self.name} is assigned to flight {flight_id} and seat {seat_id}")
        
class Pilot(Person):
    def __init__(self, name):
        super().__init__(name)
        self.role = "pilot"
        
    def be_assigned(self, flight_id, seat_id = None):
        print(f"Pilot {self.name} is assigned to flight {flight_id}")
        
class Copilot(Person):
    def __init__(self, name):
        super().__init__(name)
        self.role = "copilot"
    def be_assigned(self, flight_id, seat_id = None):
        print(f"Copilot {self.name} is assigned to flight {flight_id}")
        
class Flight_Crew(Person):
    def __init__(self, name):
        super().__init__(name)
        self.role = "flight_crew"
    def be_assigned(self, flight_id, seat_id = None):
        print(f"Flight crew member {self.name} is assigned to flight {flight_id}")