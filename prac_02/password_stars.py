def main():
    """Get and print password using a funtion."""
    password_length = 10
    password = get_password(password_length)
    print(len(password) * '*')


def get_password(password_length):
    """Get password, meets the min length."""
    password = input("Password: ")
    while len(password) < password_length:
        print("Invalid password!")
        password = input("Password: ")
    return password


main()


# def main():
#     password_length = 10
#     password = input("Password: ")
#     while len(password) < password_length:
#         print("Invalid password!")
#         password = input("Password: ")
#     print(len(password) * '*')
#
#
# main()