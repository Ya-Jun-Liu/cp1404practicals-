PASSWORD_LENGTH = 10


def main():
    """Get and print password using a funtion."""
    password = get_password(PASSWORD_LENGTH)
    print(len(password) * '*')


def get_password(password_length):
    """Get password, meets the min length."""
    password = input("Password: ")
    while len(password) < password_length:
        print("Invalid password!")
        password = input("Password: ")
    return password


main()
