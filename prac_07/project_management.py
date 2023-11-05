"""
project_management
Estimate: 1200 minutes
Actual: 1300 minutes
"""
import datetime
import csv
from project import Project

FILENAME = 'projects.txt'

# Define the constant variable for keys in the dictionary.
NAME = "name"
START_DATE = 'start_date'
PRIORITY = 'priority'
COST_ESTIMATE = 'cost_estimate'
COMPLETE_PERCENTAGE = 'complete_percentage'
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


# Define the rules that the input should not violate.

def is_not_blank(s):
    """Set condition:not blank"""
    return len(s) != 0


STRING_RULE = {is_not_blank: "Input can not be blank."}


def get_zero(y):
    """Set condition: greater than zero."""
    return y > 0


PRIORITY_RULE = {get_zero: "The priority should be greater than 0."}
COST_RULE = {get_zero: "The cost estimate should be greater than 0."}


def is_percentage(p):
    """Define percentage parameter."""
    return 100 >= p >= 0


COMPLETION_RULE = {is_percentage: "The completion percentage should be in the range of [0, 100]."}


def string_to_date(date_string):
    """Convert a date string to a date."""
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return date


def date_to_string(date):
    """Convert a date to a date string in the specified format."""
    return date.strftime("%d/%m/%Y")


def my_input(
        input_msg, type_cast=str, rules=None,
        cast_error_msg="Invalid input. Please enter again."):
    """Get a valid <type> input and return it.

    Parameters:
        input_msg (str): Show a message when asking the user for input.
        type_cast (func): A function changes a string to the type the user wants.
        rules (dict [func] -> str): Verify if the rules are acceptable.
            if not, print the corresponding error message.
        cast_error_msg: (str): It will print a message when a casting error occurs.
    Returns:
        The result of type_cast(input_msg) is returned.
    """

    index_is_ok = False
    user_input = None

    # If rules are not given, then the rules should be an empty dictionary.
    if rules is None:
        rules = {}
    while not index_is_ok:
        try:
            user_input = type_cast(input(input_msg))
            for rule, error_msg in rules.items():
                # Rule violation.
                if not rule(user_input):
                    print(error_msg)
                    break
            else:
                # If there's no rule violation, return it.
                index_is_ok = True
        except ValueError:
            # If the error occurs when casting type.
            print(cast_error_msg)
        except Exception as error_msg:
            # If an error occurs, print the error message.
            print(error_msg)

    return user_input


def load_csv_file(filename):
    """Read the rows from a csv file."""
    read_csv = []
    ignore_first_row = True
    with open(filename, newline='') as csvFile:
        for row in csv.reader(csvFile, delimiter='\t'):
            if ignore_first_row:
                ignore_first_row = False
                continue

            # Unpack each row and place it into the project constructor.
            project_info = {
                NAME: row[0],
                START_DATE: string_to_date(row[1]),
                PRIORITY: int(row[2]),
                COST_ESTIMATE: float(row[3]),
                COMPLETE_PERCENTAGE: int(row[4]),
            }
            read_csv.append(Project(**project_info))

    return read_csv


def save_csv_file(projects, filename):
    """Write the title in the first row and save the details into a csv file."""
    with open(filename, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write the first row: its property name.
        writer.writerow(["Name", "Start Date", "Priority",
                         "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                date_to_string(project.start_date),
                project.priority,
                project.cost_estimate,
                project.complete_percentage
            ])


def display_project(projects):
    """Display complete and incomplete projects."""
    print("Incomplete projects: ")
    # Filter and sort incomplete projects.
    filtered_projects = filter(Project.is_not_complete, projects)
    sorted_projects = sorted(filtered_projects, key=Project.get_priority)
    for project in sorted_projects:
        print(f"  {project}")

    # Filter and sort complete projects.
    filtered_projects = filter(Project.is_complete, projects)
    sorted_projects = sorted(filtered_projects, key=Project.get_priority)
    print("Completed projects: ")
    for project in sorted_projects:
        print(f"  {project}")


def update_project(projects):
    """Update the projects in alphabetical order, with an index number at the front."""
    for index_number, project in enumerate(projects):
        print(f"{index_number} {project}")

    def index_check(index_number_check):
        """Check if the index number falls within the valid index range."""
        return len(projects) - 1 >= index_number_check >= 0

    # Get index.
    index_rule = {index_check: f"Index out of range."}
    selected_index = my_input("Project choice: ", int, index_rule)

    # Print selected index.
    print(f"{projects[selected_index]}")

    # Get completion percentage.
    new_complete = my_input("New Percentage: ", int, COMPLETION_RULE)

    # To allow blank input, this function will change blanks to old_priority.
    old_priority = projects[selected_index].priority

    def default_int(s): return int(s) if s else old_priority

    """Convert a string to an integer. If 's' is empty, returns 'old_priority'"""

    new_priority = my_input("New Priority: ", default_int, PRIORITY_RULE)
    # Update the percentage
    projects[selected_index].complete_percentage = new_complete
    projects[selected_index].priority = new_priority


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")

    # Get information of the project.
    project_info = {
        NAME:
            my_input("Name: ", str, STRING_RULE),
        START_DATE:
            my_input("Start date (dd/mm/yy): ", string_to_date),
        PRIORITY:
            my_input("Priority: ", int, PRIORITY_RULE),
        COST_ESTIMATE:
            my_input("Cost estimate: $", float, ),
        COMPLETE_PERCENTAGE:
            my_input("Percent complete: ", int, COMPLETION_RULE)
    }
    # Update list.
    projects.append(Project(**project_info))


def filter_project(projects):
    """Filter projects by the input date."""
    threshold = my_input(
        "Show projects that start after date (dd/mm/yy): ", string_to_date)

    def filter_date_func(_project):
        """Filter if the input date is after the start date."""
        return _project.get_start_date() >= threshold

    # Filter out and sort by the date.
    filtered = filter(filter_date_func, projects)
    for project in sorted(filtered, key=Project.get_start_date):
        print(project)


def main():
    """Display a project list that allows a user to make changes using a selected menu."""

    # Load project from a csv file.
    projects = load_csv_file(FILENAME)

    # Running commands; the only choice 'Q' will trigger 'user_quit'.
    user_quit = False
    while not user_quit:

        # Print the menu string.
        print(MENU)
        # User input prompt.
        choice = input(">>> ").upper()
        if choice == "L":
            # Load - load the csv file, original projects will be discarded.
            projects = my_input("Enter a path to be loaded: ", load_csv_file)
        elif choice == 'S':
            # Save - save data as a csv file.
            # To facilitate repeated input, a mapping function is created that
            # saves a CSV file using only the filename.
            def save_csv_file2(filename):
                save_csv_file(projects, filename)

            my_input("Enter a path to be saved: ", save_csv_file2)
        elif choice == 'Q':
            # Quit - save csv to original file (FILENAME)
            save_csv_file(projects, FILENAME)
            # if quit, break the inf loop and exit the program.
            print("Thank you for using custom-built project management software.")
            user_quit = True
        elif choice == 'D':
            # Display
            display_project(projects)
        elif choice == 'A':
            # Add - add new project
            add_new_project(projects)
        elif choice == 'U':
            # Update percentage
            update_project(projects)
        elif choice == 'F':
            # Filter projects
            filter_project(projects)
        elif choice:
            print(f"GET '{choice}'")
            print("Invalid menu choice")


if __name__ == '__main__':
    main()
