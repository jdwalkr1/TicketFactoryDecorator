from abc import ABC, abstractmethod
from ticket import Ticket

class TicketDecorator(Ticket):
    #super()._init_(ticket.cost, ticket.departure, ticket.arrival)
    def __init__(self, ticket):
        self.ticket = ticket
    
    @property
    def departure(self):
        return self.ticket.departure
    
    @property
    def arrival(self):
        return self.ticket.arrival
        
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
        print(f"The cost of your ticket from {self.departure} to {self.arrival} with a snack is {self.cost} euros.")

class MealDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost + 10
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} with a meal is {self.cost} euros.")
        
class RigaTallinnTicket(TicketDecorator):
    
    def __init__(self, ticket):
        super().__init__(ticket)
        
        
    @property
    def cost(self):
        return self.ticket.cost +2
    
    