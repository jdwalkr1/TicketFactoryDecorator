
from abc import ABC, abstractmethod
from ticket import Ticket, BaseTicket, LuxuryTicket, ChildsTicket

class TicketFactory(ABC):
    @abstractmethod
    def get_Ticket(self):
        pass
   
class BaseTicketFactory(TicketFactory):
    def get_Ticket(self) -> BaseTicket:
        return BaseTicket()

class LuxuryTicketFactory(TicketFactory):
    def get_Ticket(self) -> LuxuryTicket:
        return LuxuryTicket()

class ChildTicketFactory(TicketFactory):
    def get_Ticket(self) -> ChildsTicket:
        return ChildsTicket()
    
''' Need to make decisions about implementation concerning gui'''
    