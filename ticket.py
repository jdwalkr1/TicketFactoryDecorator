from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, cost, departure, arrival):
        self.cost = cost
        self.departure = departure
        self.arrival = arrival
        
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} is {self.cost} euros")
    
    
class BaseTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(21, departure, arrival)
        
    
class LuxuryTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(28, departure, arrival)
        
    
class ChildsTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(14, departure, arrival)
        
  
    
    
    
    