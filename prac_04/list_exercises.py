"""Basic list operations."""
list_of_numbers = []
for i in range(5):
    numbers = int(input("Numbers: "))
    list_of_numbers.append(numbers)
print(
    f"Number:{list_of_numbers[0]}\nNumber:{list_of_numbers[1]}\nNumber:{list_of_numbers[2]}\nNumber:{list_of_numbers[3]}\nNumber:{list_of_numbers[4]}")
print(f"The first number is {list_of_numbers[0]}")
print(f"The last number is {list_of_numbers[-1]}")
print(f"The smallest number is {min(list_of_numbers)}")
print(f"THe largest number is {max(list_of_numbers)}")
print(f"The average of the numbers is {sum(list_of_numbers) / len(list_of_numbers)}")

"""Woefully inadequate security checker."""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")
