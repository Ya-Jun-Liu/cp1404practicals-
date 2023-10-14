"""
emails
Estimate: 50 minutes
Actual: 120 minutes
"""

"""Write a program that stores users' emails (unique keys) and names (values) in a dictionary."""


def main():
    """Create a dictionary of email-to-name."""
    email_to_name = {}  # empty dictionary
    email = input("Email: ")  # key
    while email != "":
        name = get_name_from_email(email)  # value
        confirm = input(f"Is your name {name}? (Y/n)")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name:")
        email_to_name[email] = name  # add key_value pairs into dictionary
        email = input("Email: ")

    for email, name in email_to_name.items():  # .items() return key-value pairs
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from the email entered."""
    user_name = email.split("@")[0]  # split email address at the @, take index 0 part
    name_parts = user_name.split(".")  # split user_name at the . output:['apple', 'banana'] (apple.banana@gmail.com)
    name = " ".join(name_parts).title()
    # joint name_parts into a single string with spaces in between. capitalise the first letter of each name_parts using .title()
    return name


main()
