"""
Word Occurrences
Estimate: 50 minutes
Actual: 100 minutes
"""

"""Write a program that stores users' emails (unique keys)
and names (values) in a dictionary."""


def main():
    """Create a dictionary of email-to-name."""
    email_to_name = {}  # empty dictionary
    email = input("Email: ")  # key
    while email != "":
        name = get_name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n)")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name:")
        email_to_name[email] = name  # add key_value into dictionary
        email = input("Email: ")  # value

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from the email entered."""
    user_name = email.split("@")[0]  # split email address at the @, take index 0 part
    given_name = user_name.split(".")  # split user_name at the .
    name = " ".join(
        given_name).title()  # joint given_name into a single string with spaces in between. capitalise the first letter of each given_name using .title()
    return name


main()
