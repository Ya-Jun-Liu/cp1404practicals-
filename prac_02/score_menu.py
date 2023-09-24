"""
Use a main menu following the standard menu pattern.
"""

"""
display menu
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice"
"""

menu_string = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

print(menu_string)
choice = input("> ").upper()
while choice != "Q":
    if choice == "G":
        score = int(input("Score: "))
        while score > 100 or score < 0:
            print("Invalid score")
            score = int(input("Score: "))
    elif choice == "P":
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Pass")
        else:
            print("Bad")
    elif choice == "S":
        print(score * '*')
    else:
        print("Invalid choice")
    print(menu_string)
    choice = input("> ").upper()
print("Thank you!")
