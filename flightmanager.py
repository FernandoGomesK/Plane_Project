from flight import Flight
from faker import Faker

fake = Faker('pt_BR')

class FlightManager:
    def __init__(self):
        self._flights = []
        
    def add_flight(self, flight: Flight):
        self._flights.append(flight)  
        
 