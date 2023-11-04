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
STR_RULE = {lambda s: len(s) != 0: "Input can not be blank."}
PRIORITY_RULE = {lambda y: y > 0: "Priority should be greater than 0."}
COST_RULE = {lambda y: y > 0: "Cost estimate should be greater than 0."}
COMP_RULE = {lambda y: 100 >= y >=
             0: "Completion Percentage should be in ragne [0,100]"}



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




if __name__ == '__main__':
    main()
