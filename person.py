from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def be_assigned():
        print("{self.name} was assigned")


class Passenger(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
class Flight_Crew(Person):
    def __init__(self, name):
        super().__init__(name)