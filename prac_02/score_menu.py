"""
Use a main menu following the standard menu pattern.
"""

menu_string = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get score,then print the status, stars or farewell."""
    score = get_score()
    print(menu_string)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(menu_string)
        choice = input("> ").upper()
    print("Thank you!")


def print_stars(score):
    """Print as many stars as the score."""
    print(score * '*')


def determine_status(score):
    """Determine the result status."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def get_score():
    """Get score."""
    score = int(input("Score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
