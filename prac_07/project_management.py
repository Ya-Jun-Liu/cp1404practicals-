"""
project_management
Estimate: 1200 minutes
Actual:  minutes
"""
import datetime
import csv
from project import Project

FILENAME = 'projects.txt'

# Define the constable variable for keys in dictionary
NAME = "name"
START_DATE = 'start_date'
PRIORITY = 'priority'
COST_ESTIMATE = 'cost_estimate'
COMPLETE_PERCENTAGE = 'complete_percentage'


# Define the rules that input should be not violated
def is_not_blank(s):
    """Set condition:not blank"""
    return len(s) != 0


STR_RULE = {is_not_blank: "Input can not be blank."}


def gt_zero(y):
    """Set condition: greater than zero."""
    return y > 0


PRIORITY_RULE = {gt_zero: "Priority should be greater than 0."}
COST_RULE = {gt_zero: "Cost estimate should be greater than 0."}


def is_percentage(p):
    """Define percentage parameter."""
    return 100 >= p >= 0


COMP_RULE = {is_percentage: "Completion Percentage should be in range [0,100]"}


def str_to_date(date_string):
    """Convert date string to a date."""
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return date


def date_to_str(date):
    """Convert a date to a date string in the specified format."""
    return date.strftime("%d/%m/%Y")


def main():
    """Display a project list that allows a user to add new project."""

    # Load project from csv
    projects = load_csv_file(FILENAME)

    # Run commands, only choice is Q will turn on user_quit.
    user_quit = False
    while not user_quit:

        # Print the menu string"
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        # Input prompt
        choice = input(">>> ").upper()
        if choice == "L":
            # Load csv, original projects will be discarded.
            projects = myinput("Enter a path to be loaded: ", load_csv_file)
        elif choice == 'S':
            # Save csv file

            # To input repeatedly, we write a mapping function that can
            # save csv file from only filename
            def save_csv_file2(filename):
                save_csv_file(projects, filename)

            filename = myinput("Enter a path to be saved: ", save_csv_file2)
        elif choice == 'Q':
            # Quit - Save csv to original file (FILENAME)
            save_csv_file(projects, FILENAME)
            # if quit, break the inf loop and exit the program.
            user_quit = True
        elif choice == 'D':
            # Display
            display_project(projects)
        elif choice == 'A':
            # Add new project
            add_new_project(projects)
        elif choice == 'U':
            # Update precentage
            update_project(projects)
        elif choice == 'F':
            # Filter projects
            filter_project(projects)
        elif choice:
            print(f"GET '{choice}'")
            print("Invalid manu choice")


if __name__ == '__main__':
    main()
