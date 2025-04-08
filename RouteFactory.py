from decorator import TartuTallinnDecorator, DaugavpilsRigaDecorator, DaugavpilsTallinnDecorator, DaugavpilsVilniusDecorator, DaugavpilsRigaDecorator, DaugavpilsRigaDecorator, VilniusTallinnDecorator, RigaTallinnDecorator, DaugavpilsTartuDecorator, RigaTartuDecorator, VilniusRigaDecorator, VilniusTartuDecorator 
from decorator import TicketDecorator
from ticket import Ticket 
'''frozen set provides all possible combinations of different tickets. Since tickets will be priced mutually
according to departure and destination, a set can be used in this situation'''
class RouteDecoratorFactory:
    decorators = {
        frozenset(["Tallinn", "Tartu"]): TartuTallinnDecorator,
        frozenset(["Tallinn", "Daugavpils"]): DaugavpilsTallinnDecorator,
        frozenset(["Tallinn", "Riga"]): RigaTallinnDecorator,
        frozenset(["Tallinn", "Vilnius"]): VilniusTallinnDecorator,
        frozenset(["Tartu", "Daugavpils"]): DaugavpilsTartuDecorator,
        frozenset(["Tartu", "Riga"]): RigaTartuDecorator,
        frozenset(["Tartu", "Vilnius"]): VilniusTartuDecorator,
        frozenset(["Daugavpils", "Riga"]): DaugavpilsRigaDecorator,
        frozenset(["Daugavpils", "Vilnius"]): DaugavpilsVilniusDecorator,
        frozenset(["Riga", "Vilnius"]): VilniusRigaDecorator,
    }
    '''static method retrieves Routes from set'''
    @staticmethod
    def get_route_decorator(departure: str, arrival: str, ticket: Ticket) -> TicketDecorator:
        key = frozenset([departure, arrival])
        decorator_class = RouteDecoratorFactory.decorators.get(key)
        if decorator_class:
            return decorator_class(ticket)
        else:
            raise ValueError(f"No decorator found for route: {departure} – {arrival}")
