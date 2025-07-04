from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def be_assigned():
        print("{self.name} was assigned")


class Passenger(Person):
    def __init__(self, name):
        super().__init__(name)
        
class Flight_Crew(Person):
    def __init__(self, name):
        super().__init__(name)