"""Write a program to read this file,
process the data and display processed information.
-the champions and how many times they have won.
-the countries of the champions in alphabetical order.
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read file and print the Wimbledon champions and countries"""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read records from file."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:  # Use "utf-8-sig" for reading CSV file
        in_file.readline()  # read a single line of text in the file and returns it as a string
        for line in in_file:  # iterates over the remaining lines in the file
            parts = line.strip().split(",")  # remove whitespace, split the line into a list of parts using comma
            records.append(parts)  # store each line of data as a list of values into the records list
    return records


def process_records(records):
    """Create a champion_to_count dictionary."""
    champion_to_count = {}  # empty dictionary
    countries = set()  # empty set, ensure that each country is included only once
    for record in records:  # iterate through the records list
        countries.add(record[INDEX_COUNTRY])  # add unique country name to the countries set
        if record[INDEX_CHAMPION] in champion_to_count:  # true when the champion name is in the dictionary
            champion_to_count[record[INDEX_CHAMPION]] += 1  # add one to count
        else:
            champion_to_count[record[INDEX_CHAMPION]] = 1
            # first time see the champion name, add the name as a key in the dictionary, set its count to one
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Print champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(f"{name} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(",".join(country for country in sorted(countries)))


main()
