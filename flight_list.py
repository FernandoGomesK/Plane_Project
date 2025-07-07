from flight import Flight
from person import Passenger
from faker import Faker

fake = Faker()

class flight_list:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)  
        
    def initialize(self, flights = 5, passenger_number = 2 ):
        for i in range(flights):
            fly = Flight(passenger_number)
            self.add_flight(fly)
            passengers = [Passenger(fake.name()) for x in range(passenger_number)]
            for p in passengers:
                fly.assign_passenger(p)   
            fly.display_manifest()
        
 