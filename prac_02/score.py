"""
CP1404 - Practical program to determine score status
"""

import random

def main():
    """Get user's score and print result."""
    score = float(input("Score: "))
    print(f"Entered score {score} is '{determine_status(score)}'.")
    """Generate random score and print result."""
    score = random.randint(0, 100)
    print(f"Random score is {score}. \nThe status is '{determine_status(score)}'.")


def determine_status(score):
    """Determine status of a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
