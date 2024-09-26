from prac_09.car import Car
from random import randint


class UnreliableCar(Car):  # overrides class Car
    """An unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the random number is below the reliability level of the car."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        # call the drive method of the parent class, passing the distance
        distance_driven = super().drive(distance)
        return distance_driven

