from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, departure, arrival, departure_datetime, cost=0):
        self.departure = departure
        self.arrival = arrival
        self.departure_datetime = departure_datetime
        self._cost = cost
   
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
    def __init__(self, departure, arrival, departure_datetime):
        super().__init__(departure, arrival, departure_datetime, 21)
    
    def printCost(self):
        print(f"Ticket from {self.departure} to {self.arrival} on {self.departure_datetime} costs {self.cost} EUR")
        
class BasicTicket(Ticket):
    def __init__(self, departure, arrival, departure_datetime, cost=0):
        self._departure = departure
        self._arrival = arrival
        self._departure_datetime = departure_datetime
        self._cost = cost

    @property
    def departure(self):
        return self._departure

    @property
    def arrival(self):
        return self._arrival

    @property
    def cost(self):
        return self._cost

    @property
    def departure_datetime(self):
        return self._departure_datetime

    def printCost(self):
        print(f"The basic ticket from {self.departure} to {self.arrival} costs {self.cost} euros, departing at {self.departure_datetime}.")

'''          
class LuxuryTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(28, departure, arrival)
           
class ChildsTicket(Ticket):
    def __init__(self, departure, arrival):
        super().__init__(14, departure, arrival)
   '''     
  
    
    
    
    