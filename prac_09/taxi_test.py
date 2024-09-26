"""
taxi_test
Estimate: 30 minutes
Actual: 50 minutes
"""
# client code

from prac_09.taxi import Taxi


def main():
    """Test for Taxi class."""
    my_taxi = Taxi("Prius 1", 100)  # object
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
