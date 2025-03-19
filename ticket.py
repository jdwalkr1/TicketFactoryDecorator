from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, cost):
        self.cost = cost
        
    
    def cost(self):
        pass
    
    
class BaseTicket(Ticket):
    def __init__(self):
        super().__init__(21)
        
    def printCost(self):
        print(f"The cost of your ticket is {self.cost} euros")
    
class LuxuryTicket(Ticket):
    def __init__(self):
        super().__init__(28)
        
    def printCost(self):
        print(f"The cost of your ticket is {self.cost} euros")
    
class ChildsTicket(Ticket):
    def __init__(self):
        super().__init__(14)
        
    def printCost(self):
        print(f"The cost of your ticket is {self.cost} euros")
    
    
    
    
    
    
    