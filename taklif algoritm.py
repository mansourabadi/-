def car_menu():
    print("1. Iranian Cars")
    print("2. Foreign Cars")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        iranian_cars()
    elif choice == "2":
        foreign_cars()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
        car_menu()


def iranian_cars():
    print("1. Iran Khodro")
    print("2. Saipa")
    print("3. Back")

    choice = input("Enter your choice: ")
    if choice == "1":
        iran_khodro_cars()
    elif choice == "2":
        saipa_cars()
    elif choice == "3":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        iranian_cars()


def foreign_cars():
    print("1. Toyota")
    print("2. Honda")
    print("3. Back")

    choice = input("Enter your choice: ")
    if choice == "1":
        toyota_cars()
    elif choice == "2":
        honda_cars()
    elif choice == "3":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        foreign_cars()


def iran_khodro_cars():
    print("1. pegu 207")
    print("2. pars")
    print("3.dena+")
    print("4. Back")
    print("5. main menu")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected pegu 207")
    elif choice == "2":
        print("You selected pars")
    elif choice == "3":
        print("You selected dena+")
    elif choice == "4":
        iranian_cars()
    elif choice == "5":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        iran_khodro_cars()


def saipa_cars():
    print("1. saina")
    print("2. Quick")
    print("3. Back")
    print("4. main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected saina")
    elif choice == "2":
        print("You selected Quick")
    elif choice == "3":
        iranian_cars()
    elif choice == "4":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        saipa_cars()


def toyota_cars():
    print("1. Camry")
    print("2. Corolla")
    print("3. Back")
    print("4. main menu")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected Camry")
    elif choice == "2":
        print("You selected Corolla")
    elif choice == "3":
        foreign_cars()
    elif choice == "4":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        toyota_cars()


def honda_cars():
    print("1. Civic")
    print("2. Accord")
    print("3. Back")
    print("4. main menu")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected Civic")
    elif choice == "2":
        print("You selected Accord")
    elif choice == "3":
        foreign_cars()
    elif choice == "4":
        car_menu()
    else:
        print("Invalid choice. Please try again.")
        honda_cars()


car_menu()