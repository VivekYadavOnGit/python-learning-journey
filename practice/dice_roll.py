import random

def dice_roll(n):
    rolls = []
    for _ in range(n):
        rolls.append(random.randint(1, 6))
    return rolls

def main():
    n = int(input("Enter the number of times to roll the dice: "))
    rolls = dice_roll(n)
    print(f"Dice rolls: {rolls}")

    print ("Number of times each face appeared:")
    for i in range(1, 7):
        count = rolls.count(i)
        print(f"Face {i}: {count} times")

main()