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

    def __lt__(self, other):
        """Compare guitars by year."""
        return self.year < other.year


def load_csv_file(filename):
    """Load the guitar list from a csv file."""
    read_row = []
    with open(filename, newline='') as csvfile:
        for row in csv.reader(csvfile):
            # unpack each row and put it into Guitar constructor
            name, year, cost = row
            read_row.append(Guitar(name, int(year), float(cost)))
    return read_row


def display_guitars(guitars):
    """Display guitar list."""
    for guitar in guitars:
        print(guitar)


def save_csv_file(guitars, filename):
    """Save guitar list to a csv file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"Save guitars into {filename}.csv successfully.")


def get_nonempty_string(input_msg):
    """Get a valid string and return to main."""

    get_name = input(input_msg)  # input_msg (str): Show message when ask user to input.
    while get_name == '':
        print("Input can not be blank.")
        get_name = input(input_msg)
    return get_name  # an input string


def main():
    """Display a guitar list that allows a user to add new guitar."""

    # Load Songs from csv
    guitars = load_csv_file(FILENAME)
    # Sort the guitars
    guitars.sort()

    # Run commands, only choice is Q will turn on user_quit.
    user_quit = False
    while not user_quit:
        # Print the menu string
        print("Menu:")
        print("D - Display guitars")
        print("A - Add new guitar")
        print("Q - Quit")

        # Input prompt
        choice = input(">>> ").upper()


if __name__ == '__main__':
    main()
