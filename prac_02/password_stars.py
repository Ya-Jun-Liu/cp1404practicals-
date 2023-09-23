password_length = 10
password = input("Password: ")
while len(password) < password_length:
    print("Invalid password!")
    password = input("Password: ")
print(len(password) * '*')
