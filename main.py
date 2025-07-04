from flight import Flight

class Flight_rows:
    def __init__(self):
        self.flights = [Flight() for x in range(10)]
        
    def show_flights(self):
        for f in self.flights:
            f.show_id()
            
vous = Flight_rows()
