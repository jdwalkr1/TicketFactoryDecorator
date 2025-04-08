from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, cost, departure, arrival, departure_datetime):
        self._cost = cost
        self.departure = departure
        self.arrival = arrival
        self.departure = departure_datetime 
         
    @property
    def cost(self):
        return self._cost 
    
    @cost.setter
    def cost(self, value):
        self._cost = value
        
    @abstractmethod
    def printCost(self):
        pass
        
    
class BaseTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(21, departure, arrival)
    
    def printCost(self):
        print(f"Ticket from {self.departure} to {self.arrival} on {self.departure_datetime} costs {self.cost} EUR")
'''          
class LuxuryTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(28, departure, arrival)
           
class ChildsTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(14, departure, arrival)
   '''     
  
    
    
    
    