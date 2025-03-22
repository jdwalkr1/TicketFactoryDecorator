# main.py
from factory import BaseTicketFactory, LuxuryTicketFactory, ChildTicketFactory
from decorator import SnackDecorator

def read_tickets(ticket_type):
    factories = {
        "Adult": BaseTicketFactory(),
        "Luxury": LuxuryTicketFactory(),
        "Child": ChildTicketFactory(),
    }

    if ticket_type in factories:
        factory = factories[ticket_type]
        ticket = SnackDecorator(factory.get_Ticket())
        ticket.printCost()  
        return ticket
    else:
        print("Incorrect Entry. Please Try Again.")
        return None

def main():
    ticket = read_tickets("Luxury") 
    if ticket:
        print("Ticket successfully created.")

if __name__ == '__main__':
    main()
