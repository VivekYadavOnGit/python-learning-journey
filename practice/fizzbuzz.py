# FizzBuzz:
# Print numbers 1–100.
# Multiples of 3 → Fizz
# Multiples of 5 → Buzz
# Multiples of both → FizzBuzz
# Otherwise → print the number.

def fizz_buzz():
    
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

fizz_buzz()