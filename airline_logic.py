from airline_data import flights, bookings


# Show flights
def show_flights():
    print("\nAvailable Flights:")
    for code, info in flights.items():
        print(f"{code} → {info['destination']} | Seats: {info['seats']}")


# Book ticket
def book_ticket():
    name = input("Enter passenger name: ")
    flight = input("Enter flight code: ")

    if flight in flights and flights[flight]["seats"] > 0:
        flights[flight]["seats"] -= 1
        bookings[name] = flight
        print("Ticket booked successfully!")
    else:
        print("Flight not available or no seats left!")


# Cancel ticket
def cancel_ticket():
    name = input("Enter passenger name: ")

    if name in bookings:
        flight = bookings[name]
        flights[flight]["seats"] += 1
        del bookings[name]
        print("Ticket cancelled successfully!")
    else:
        print("No booking found!")


# Show bookings
def show_bookings():
    print("\nBooking Records:")

    if len(bookings) == 0:
        print("No bookings yet.")
    else:
        for name, flight in bookings.items():
            print(f"{name} → {flight}")