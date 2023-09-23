PASSWORD_LENGTH = 10


def main():
    """Get and print as many stars as password characters."""
    password = input("Password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password!")
        password = input("Password: ")
    print(len(password) * '*')


main()
