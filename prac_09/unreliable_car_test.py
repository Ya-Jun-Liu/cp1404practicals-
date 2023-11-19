"""
CP1404/CP5632 Practical
UnreliableCar class tests

A good car should drive more often than the bad car.
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test class UnreliableCar."""

    # cars with different reliabilities
    good_car = UnreliableCar("Good car", 100, 90)
    bad_car = UnreliableCar("Bad car", 100, 9)

    # drive both cars multiple times
    # print the distance they drove
    for i in range(1, 5):
        print(f"Drive {i}km:")
        print(f"{good_car.name:10} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:10} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()

