import airline_logic

while True:
    print("\n===== AIRLINE MENU =====")
    print("1. View Flights")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Bookings")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        airline_logic.show_flights()

    elif choice == "2":
        airline_logic.book_ticket()

    elif choice == "3":
        airline_logic.cancel_ticket()

    elif choice == "4":
        airline_logic.show_bookings()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")