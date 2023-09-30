"""
Type in the following in console
import random
print(random.uniform(2.5, 5.5))
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# 5,20


# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# 3, 9, NO


# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.536589126820833
# The largest number is 5.458676414415265


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
random_number = (random.randint(1,100))
print(random_number)
