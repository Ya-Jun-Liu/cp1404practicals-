PASSWORD_LENGTH = 10


def main():
    """Get and print password using functions."""
    password = get_password(PASSWORD_LENGTH)
    print_stars(password)


def print_stars(password):
    """Print as many stars as the password length."""
    print(len(password) * '*')


def get_password(password_length):
    """Get password, meeting the minimum length requirement."""
    password = input("Password: ")
    while len(password) < password_length:
        print("Invalid password!")
        password = input("Password: ")
    return password


main()
