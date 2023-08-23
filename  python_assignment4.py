class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

flights = [
    Flight("AI161E90", "BLR", "BOM", 5600),
    Flight("BR161F91", "BOM", "BBI", 6750),
    Flight("AI161F99", "BBI", "BLR", 8210),
    Flight("VS171E20", "JLR", "BBI", 5500),
    Flight("AS171G30", "HYD", "JLR", 4400),
    Flight("AI131F49", "HYD", "BOM", 3499)
]

user_input = input("Enter a flight ID, source city, or destination city: ")

matching_flights = []

for flight in flights:
    if (
        user_input == flight.flight_id
        or user_input == flight.source
        or user_input == flight.destination
    ):
        matching_flights.append(flight)

if matching_flights:
    for flight in matching_flights:
        print("Flight ID:", flight.flight_id)
        print("Source:", flight.source)
        print("Destination:", flight.destination)
        print("Price:", flight.price)
else:
    print("No matching flights found.")
