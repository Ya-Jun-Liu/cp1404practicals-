# Q1 Write code that asks the user for their name,
# then opens a file called "name.txt"
# and writes that name to it.
# Remember to close your file.
out_file = open("name.txt", "w")
user_name = input("Enter your name: ")
print(user_name, file = out_file)
out_file.close()


# Q2 Write code that opens "name.txt"
# and reads the name (as above) then prints,
# "Your name is Bob"
with open("name.txt", "r") as out_file:
    for line in out_file:
        print(f"\"Your name is {user_name}\"")