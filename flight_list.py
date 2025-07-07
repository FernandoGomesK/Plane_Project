from flight import Flight
from person import Passenger, Pilot, Copilot 
from faker import Faker

fake = Faker('pt_BR')

class flight_list:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)  
        
    def initialize(self, flights = 2, passenger_number = 100 ):
        for i in range(flights):
            fly = Flight(passenger_number)
            self.add_flight(fly)
            pilot = [Pilot(fake.name()) for x in range(1)]
            copilot = [Copilot(fake.name()) for x in range(1)]
            fly.assign_crew(pilot[0], copilot[0])
            passengers = [Passenger(fake.name()) for x in range(passenger_number)]
            for p in passengers:
                fly.assign_passenger(p)   
            fly.display_manifest()
        
 