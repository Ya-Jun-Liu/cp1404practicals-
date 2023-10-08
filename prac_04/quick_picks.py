import random

NUMBER_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick pick lottery ticket generator program."""
    number_of_picks = int(input("Number of quick picks: "))
    while number_of_picks < 0:
        print("Invalid number.")
        number_of_picks = int(input("Number of quick picks: "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
