"""
Q1. Pseudocode
open a file called "name.txt"
ask the user for their name
write user's name to the file
close file.
"""

# out_file = open("name.txt", "w")
# user_name = input("Enter your name: ")
# print(user_name, file=out_file)
# out_file.close()
#
# """
# Q2. Pseudocode
# open "name.txt"
# reads the name (as above)
# prints "Your name is Bob"
# """
#
# with open("name.txt", "r") as out_file:
#     for line in out_file:
#         print(f"\"Your name is {user_name}\"")

"""
Q3. Pseudocode
Create a text file called "numbers.txt"
save it in your prac directory
open "numbers.txt", 
read only the first two numbers
add them together 
print the result
"""

# in_file = open("numbers.txt", "r")
# total = 0
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# in_file.close()
# print(number1 + number2)

"""
Q4.
print the total for all lines in numbers.txt
"""

with open("numbers.txt", "r") as in_file:
    numbers = in_file.readlines()
    total = 0
    for line in numbers:
        total += int(line)
    print(total)
