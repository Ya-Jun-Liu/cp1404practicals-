"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode
get sales
while sales >= 0
    calculate bonus
    get sales
Print bonus
"""

sales = float(input("Enter sales: $"))
bonus = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Your bonus is $", bonus)
    sales = float(input("Enter sales: $"))
print("Thanks for using this program!")



