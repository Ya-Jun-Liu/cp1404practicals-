"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)

Language_file_reader
Estimate: 240 minutes
Actual: 300 minutes
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read a file containing programming language details, save them as objects, and display the information."""
    languages = []
    # Open the file for reading.
    in_file = open('languages.csv', 'r')
    # File format : Language,Typing,Reflection,Year
    # Consume the first line (header) - its contents are not needed.
    in_file.readline()
    # All other lines contain language data. Use a for loop to read the rest of the file.
    for line in in_file:
        # Print(repr(line))  # debugging
        # Remove the last newline and split it into CSV parts
        parts = line.strip().split(',')
        # Print(parts)  # debugging
        # The reflection is stored as a string (Yes/No), and we want it as a Boolean.
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[3] == "Yes"
        # Create a ProgrammingLanguage object using the provided elements.
        # Year should be an int.
        language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[3]))
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # To avoid quoted \n in strings being considered a new record.
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # Use the default Excel dialect.
    for row in reader:
        print(row)
    in_file.close()


# using_csv()


def using_namedtuple():
    """Create a language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    # Language will be a new subclass of the tuple data type class
    Language = namedtuple('Language', 'name, typing, reflection,pointer_arithmetic, year')
    reader = csv.reader(in_file)  # use default Excel dialect

    for row in reader:
        # print(row)
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()


def using_csv_namedtuple():
    """Create a language file reader version using both the CSV module and a named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection,pointer_arithmetic, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()
