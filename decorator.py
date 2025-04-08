from abc import ABC, abstractmethod
from ticket import Ticket

'''Ticket Decorators add pricing according to Departure-Destination Pairs, pricing is mutual from Departure and 
Destination. For example, Tallinn to Tartu is the same price as Tartu to Tallinn'''
class TicketDecorator(Ticket):
    
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
    
    @property
    def departure_datetime(self):
        return self.ticket.departure_datetime 
    
    def printCost(self):
        self.ticket.printCost()
    
class SnackDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost + 5
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} with a snack is {self.cost} euros.")

class MealDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost + 10
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} with a meal is {self.cost} euros.")
        
class LuxuryDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost + 7
    
    def printCost(self):
        print(f"The cost of your luxury ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
        
class ChildDecorator(TicketDecorator):
    @property
    def cost(self):
        return self.ticket.cost - 7
    
    def printCost(self):
        print(f"The cost of your child's ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
           
class RigaTallinnDecorator(TicketDecorator):
       
    @property
    def cost(self):
        return self.ticket.cost +2
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
        
class TartuTallinnDecorator(TicketDecorator):
    
    @property
    def cost(self):
        return self.ticket.cost 
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
        
class DaugavpilsTallinnDecorator(TicketDecorator):
    
    @property
    def cost(self):
        return self.ticket.cost + 4 
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")

class VilniusTallinnDecorator(TicketDecorator):
    
    @property
    def cost(self):
        return self.ticket.cost + 5 
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")

class DaugavpilsTartuDecorator(TicketDecorator):
    
    @property
    def cost(self):
        return self.ticket.cost + 4
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")

class RigaTartuDecorator(TicketDecorator):
     
    @property
    def cost(self):
        return self.ticket.cost + 2
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
        
class VilniusTartuDecorator(TicketDecorator):
       
    @property
    def cost(self):
        return self.ticket.cost + 5
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")

class VilniusRigaDecorator(TicketDecorator):
    
    #def __init__(self, ticket):
    #    super().__init__(ticket)    
    @property
    def cost(self):
        return self.ticket.cost +2
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")

class DaugavpilsRigaDecorator(TicketDecorator):
       
    @property
    def cost(self):
        return self.ticket.cost 
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")
        
class DaugavpilsVilniusDecorator(TicketDecorator):
    
    @property
    def cost(self):
        return self.ticket.cost 
    
    def printCost(self):
        print(f"The cost of your ticket from {self.departure} to {self.arrival} departing at {self.departure_datetime} is {self.cost} euros.")