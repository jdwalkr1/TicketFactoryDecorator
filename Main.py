from factory import TicketFactory, BaseTicketFactory, LuxuryTicketFactory, ChildTicketFactory
from ticket import Ticket, BaseTicket, LuxuryTicket, ChildsTicket

def read_tickets(string) -> Ticket:
   factories = {
       "Adult": BaseTicketFactory(),
       "Luxury": LuxuryTicketFactory(),
       "Child": ChildTicketFactory(),
   }
   
   while True:
       #ticket_choice = input("Enter your ticket (Adult, Luxury, Child): ")
       if string in factories:
           fact = factories[string]
           ticket = fact.get_Ticket()
           ticket.printCost()
           break
       else:
           print("Incorrect Entry. Please Try Again.")
           return None
           

def main():
    fac = read_tickets("Adult")
    if fac:
        print("Ticket successfully created.")
   
if __name__ == '__main__':
    main()