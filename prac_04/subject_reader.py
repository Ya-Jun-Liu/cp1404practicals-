"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)  # add parts(type:list) into data(type:list)
    input_file.close()
    return data


def display_data(data):
    """Display subject details."""
    for i in range(len(data)):
        # print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")
        print("{:6} is taught by {:12} and has {:3} students".format(data[i][0], data[i][1], data[i][2]))


main()
