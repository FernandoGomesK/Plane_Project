from flight import Flight
from person import Passenger
from faker import Faker
from flight_list import flight_list

fake = Faker('pt_BR')
        
# test_run()
def real_run():
    list_fly = flight_list()
    list_fly.initialize()
    
real_run()