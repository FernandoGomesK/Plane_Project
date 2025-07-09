import random
from seat import Seat
from person import Passenger, FlightCrew
import uuid
from typing import List

class Flight:
    def __init__(self, total_seats: int):
        """
        Constructor for Flight class.

        Args:
            total_seats (int): Total number of seats on the flight.

        Attributes:
            _flight_id (str): Unique identifier for the flight.
            _total_seats (int): Total number of seats on the flight.
            _pilot (FlightCrew): Pilot of the flight.
            _copilot (FlightCrew): Copilot of the flight.
            _cabin_crew (list[FlightCrew]): List of cabin crew members.
            _seats (list[Seat]): List of all seats on the flight.
        """
        self._flight_id = str(uuid.uuid4())[:4]
        self._total_seats = total_seats
        self._pilot = None
        self._copilot = None
        self._cabin_crew = List[FlightCrew]
        self._seats = [Seat(i) for i in range(1, total_seats + 1)]
        
    @property
    def flight_id(self):
        
        return self._flight_id

    def show_seats(self):
        """
        Displays information about all seats on the flight.
        """
        for s in self.seats:
            print(f"flight id: {self.flight_id}")
            s.show_seat_info()
            
    def assign_crew(self, pilot: FlightCrew, copilot: FlightCrew, cabin_crew: list[FlightCrew]):
        """
        Assigns a crew to the flight.

        Args:
            pilot (FlightCrew): Pilot of the flight.
            copilot (FlightCrew): Copilot of the flight.
            cabin_crew (list[FlightCrew]): List of cabin crew members.
        """
        self._pilot = pilot
        self._copilot = copilot
        self._cabin_crew = cabin_crew
        pilot.be_assigned(self.flight_id)
        copilot.be_assigned(self.flight_id)
        for c in cabin_crew:
            c.be_assigned(self.flight_id)
    def assign_passenger(self, passenger: Passenger):
        """
        Assigns a passenger to an available seat on the flight.

        Args:
            passenger (Passenger): Passenger to be assigned.

        Returns:
            bool: True if the passenger was assigned, False otherwise.
        """
        for seat in self._seats:
            if seat.assign(passenger):
                passenger.be_assigned(self.flight_id, seat.seat_id)
                return True
        return False
    
    def count_occupied_seats(self):
        return sum(1 for seat in self._seats if seat.is_occupied)


    def aleatory_passenger_choose(self):
        occupied_seat_list = [seat for seat in self._seats if seat.is_occupied]
        sample_size = min(10, len(occupied_seat_list))
        if sample_size > 0:
            return random.sample(occupied_seat_list, sample_size)
        return []
                
    def display_manifest(self):
        print("-" * 30)
        print(f" flight manifest: {self.flight_id}")
        print(f"pilot: {self._pilot.name} | copilot: {self._copilot.name}")
        print(f"cabin crew: {[c.name for c in self._cabin_crew]}")
        print("-" * 30)
        print(f" total seats: {self._total_seats} | occupied seats: {self.count_occupied_seats()}")
        
        passenger_sample = self.aleatory_passenger_choose()
        if passenger_sample:
            for seat in passenger_sample:
                seat.show_seat_info()
        print("-" * 30)
   