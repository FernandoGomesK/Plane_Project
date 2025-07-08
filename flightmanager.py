from flight import Flight
from person import Passenger, Pilot, Copilot 
from faker import Faker

fake = Faker('pt_BR')

class FlightManager:
    def __init__(self):
        self._flights = []
        
    def add_flight(self, flight: Flight):
        print(f"flight {flight.flight_id} added")
        self._flights.append(flight)  
        
 