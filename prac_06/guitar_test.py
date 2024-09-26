"""
languages
Estimate: 30 minutes
Actual: 30 minutes
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2023


def test():
    """Test for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2013)

    print(f"{guitar.name} get_age() - Expected {101}. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected {10}. Got {another.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {False}. Got {another.is_vintage()}")


if __name__ == '__main__':
    test()
