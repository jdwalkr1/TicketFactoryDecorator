# main.py
'''All of this needs to be refactored'''

'''Must be refactored - Ticket factory now only produces base ticket, Luxury and Child's ticket now are decorators '''
'''def read_tickets(ticket_type):
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
'''