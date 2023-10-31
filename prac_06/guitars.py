"""
languages
Estimate: 30 minutes
Actual: 60 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Store input guitar details and print it."""
    guitars = []  # empty list to store user input

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost:$ "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    if guitars:  # list(guitars) not empty
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""  # initialize an empty string
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0} : {1.name:>20} ({1.year}), worth ${1.cost:10.2f}{2}".format(i, guitar, vintage_string))

    else:
        print("No guitar : (Let's go and buy one!)")


main()
