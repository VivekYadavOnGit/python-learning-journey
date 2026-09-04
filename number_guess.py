import random


def main():
    print("Think of a number between 1 and 20.")
    print("I will try to guess it!")

    attempts = guess_number()

    print(f"I guessed your number in {attempts} attempts!")


def guess_number():
    low = 1
    high = 20
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\nIs your number {guess}?")
        response = input("Enter H (higher), L (lower), or C (correct): ").lower()

        if response == "c":
            print("🎉 I got it!")
            return attempts

        elif response == "h":
            low = guess + 1

        elif response == "l":
            high = guess - 1

        else:
            print("Invalid input. Please enter H, L, or C.")


main()