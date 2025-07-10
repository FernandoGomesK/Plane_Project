import random
from flight import Flight
from faker import Faker
from flightmanager import FlightManager
from person import Passenger, FlightCrew
from planemodel import AirplaneModel


def run_system():
    fake = Faker('pt_BR')
    airline = FlightManager()
    
    num_flights = 10

    available_models = list(AirplaneModel)
      
    for i in range(num_flights):
        plane_model = random.choice(available_models)
        flight = Flight(plane_model = plane_model)
        
        passengers = flight.total_seats
        
        airline.add_flight(flight)
        print(f"flight {flight.flight_id} added")
        pilot = FlightCrew(fake.name(), role = "pilot")
        copilot = FlightCrew(fake.name(), role = "copilot")
        cabin_crew = [FlightCrew(fake.name(), role = "cabin crew") for x in range(3)]
        
        flight.assign_crew(pilot, copilot, cabin_crew)

        passenger_list = [Passenger(fake.name()) for x in range(passengers)]
        for p in passenger_list:
            if not flight.assign_passenger(p):
                print(f"flight full {p.name}")
                break
            
        flight.display_manifest()   
        