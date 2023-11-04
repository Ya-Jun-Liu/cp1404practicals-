"""
myguitars
Estimate: 300 minutes
Actual: 720 minutes
"""


import csv

CURRENT_YEAR = 2023
VINTAGE = 50
FILENAME = 'guitars.csv'


class Guitar:
    """Store guitar information."""

    def __init__(self, name="", year=0, cost=0):
        """Guitar initial information."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format."""
        return f"{self.name:30} ({self.year}) : ${self.cost:10.2f}"

    def get_age(self):
        """Ger age of a guitar based on CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is a vintage and return a Boolean."""
        return self.get_age() >= VINTAGE




def load_csv_file(filename):
    """Load csv file."""
    read_row = []
    with open(filename, newline='') as csvfile:
        for row in csv.reader(csvfile):
            # unpack each row and put it into Guitar constructor
            name, year, cost = row
            read_row.append(Guitar(name, int(year), float(cost)))
    return read_row


def display_guitars(guitars):
    """Display information of guitars."""
    for guitar in guitars:
        print(guitar)

def main():
    """Display a guitar list that allows a user to add new guitar."""

    # Load Songs from csv
    guitars = load_csv_file(FILENAME)
    # Sort the guitars
    guitars.sort()









if __name__ == '__main__':
    main()
