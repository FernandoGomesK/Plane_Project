from flight import Flight
from faker import Faker
from flightmanager import FlightManager
from person import Passenger, Pilot, Copilot


        
# test_run()
 # def real_run():
    #list_fly = FlightManager()
    #list_fly.initialize()
    
# real_run()


def run_script():
    fake = Faker('pt_BR')
    airline = FlightManager()
    
    num_flights = 2
    seats_per_flight = 20
    passengers = 20
    
    for i in range(num_flights):
        flight = Flight(total_seats = seats_per_flight)
        airline.add_flight(flight)
        
        flight.assign_crew(Pilot(fake.name()), Copilot(fake.name()))
        
        passenger_list = [Passenger(fake.name()) for x in range(passengers)]
        for p in passenger_list:
            if not flight.assign_passenger(p):
                print(f"flight full {p.name}")
                break
            
        flight.display_manifest()   
        
if __name__ == "__main__":
    run_script()