from flask import Flask, render_template, request
from ticket import BaseTicket
from decorator import (SnackDecorator, MealDecorator, LuxuryDecorator, ChildDecorator,
                         RigaTallinnDecorator, TartuTallinnDecorator, DaugavpilsTallinnDecorator,
                         VilniusTallinnDecorator, DaugavpilsTartuDecorator, RigaTartuDecorator,
                         VilniusTartuDecorator, VilniusRigaDecorator, DaugavpilsRigaDecorator,
                         DaugavpilsVilniusDecorator)

from datetime import datetime

app = Flask(__name__)

# Define available routes (departure, arrival) and map them to Decorators
ROUTE_DECORATORS = {
    ("Riga", "Tallinn"): RigaTallinnDecorator,
    ("Tallinn", "Riga"): RigaTallinnDecorator,
    ("Tartu", "Tallinn"): TartuTallinnDecorator,
    ("Tallinn", "Tartu"): TartuTallinnDecorator,
    ("Daugavpils", "Tallinn"): DaugavpilsTallinnDecorator,
    ("Tallinn", "Daugavpils"): DaugavpilsTallinnDecorator,
    ("Vilnius", "Tallinn"): VilniusTallinnDecorator,
    ("Tallinn", "Vilnius"): VilniusTallinnDecorator,
    ("Daugavpils", "Tartu"): DaugavpilsTartuDecorator,
    ("Tartu", "Daugavpils"): DaugavpilsTartuDecorator,
    ("Riga", "Tartu"): RigaTartuDecorator,
    ("Tartu", "Riga"): RigaTartuDecorator,
    ("Vilnius", "Tartu"): VilniusTartuDecorator,
    ("Tartu", "Vilnius"): VilniusTartuDecorator,
    ("Vilnius", "Riga"): VilniusRigaDecorator,
    ("Riga", "Vilnius"): VilniusRigaDecorator,
    ("Daugavpils", "Riga"): DaugavpilsRigaDecorator,
    ("Riga", "Daugavpils"): DaugavpilsRigaDecorator,
    ("Daugavpils", "Vilnius"): DaugavpilsVilniusDecorator,
    ("Vilnius", "Daugavpils"): DaugavpilsVilniusDecorator,
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        departure = request.form["departure"]
        arrival = request.form["arrival"]
        extras = request.form.getlist("extras")  # List of selected extras
        
        # Create basic ticket
        ticket = BaseTicket(departure, arrival, departure_datetime=datetime.now())

        
        # Apply route decorator
        route_key = (departure, arrival)
        if route_key in ROUTE_DECORATORS:
            ticket = ROUTE_DECORATORS[route_key](ticket)
        
        # Apply extras
        if "snack" in extras:
            ticket = SnackDecorator(ticket)
        if "meal" in extras:
            ticket = MealDecorator(ticket)
        if "luxury" in extras:
            ticket = LuxuryDecorator(ticket)
        if "child" in extras:
            ticket = ChildDecorator(ticket)
        
        final_cost = ticket.cost
        return render_template("results.html", ticket=ticket, final_cost=final_cost)
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
