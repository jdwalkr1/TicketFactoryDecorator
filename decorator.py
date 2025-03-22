from abc import ABC, abstractmethod
from ticket import Ticket

class TicketDecorator(Ticket):
    def __init__(self, ticket):
        self.ticket = ticket
        
    @property
    def cost(self):
        return self.ticket.cost 
    
    def printCost(self):
        self.ticket.printCost()
    
class SnackDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost + 5
    
    def printCost(self):
        print(f"The cost of your ticket with a snack is {self.cost} euros.")