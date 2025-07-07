from flight import Flight
from person import Passenger
from faker import Faker

fake = Faker()

class flight_list:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)  
    def initialize(self):
        
        for i in range(5):
            fly = Flight(2)
            self.add_flight(fly)
            passengers = [Passenger(fake.name()) for x in range(2)]
            
            
            for p in passengers:
                fly.assign_passenger(p)
                
            fly.display_manifest()
        
 