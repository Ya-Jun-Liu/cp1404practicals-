"""
prac09-taxi_simulator
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Let the user choose a taxi, enter the distance, and display the cost."""
    print("Let's drive!")
    print(MENU)
    current_taxi = ""
    taxis = display_taxis()
    bill = 0
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis, bill, current_taxi)
        elif choice == "d":
            if current_taxi != "":
                bill += drive_distance(current_taxi)
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid option.")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def display_taxis():
    """Display the list of taxis."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    return taxis


def choose_taxi(taxis, bill, current_taxi):
    """Choose a taxi."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    current_taxi = None
    max_number = len(taxis)
    number_is_valid = False
    while not number_is_valid:
        try:
            taxi_number = int(input("Choose taxi:"))

            if 0 == taxi_number <= max_number:
                number_is_valid = True
                current_taxi = taxis[taxi_number]
            else:
                print("Invalid taxi choice")
                print(f"Bill to date: ${bill:.2f}")
        except ValueError:
            print("Invalid input; enter a valid number.")
    return current_taxi


def drive_distance(taxi):
    """Display bill."""
    distance = int(input("Drive how far?"))
    taxi.drive(distance)
    print(f"Your {taxi.name} trip cost you: ${taxi.get_fare():.2f}")
    return taxi.get_fare()


if __name__ == '__main__':
    main()
