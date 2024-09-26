number_of_items = int(input("Enter number of items: "))
total = 0

# if statement only executes once correctly. Second entry it prints the last line
# without line 8, it will not stop print line 7
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter number of items: "))

for i in range(number_of_items):
    price = float(input("Enter price of item:$ "))
    total += price

if total > 100:
    total = total * 0.9


print(f"Total price for {number_of_items} items is ${total:.2f}")
