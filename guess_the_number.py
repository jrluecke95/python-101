import random

print("I am thinking of a number")
number = random.randint(1, 10)
guess = 0

while (guess != number):
    guess = int(input("What is your guess? "))
    if (guess < number):
        print(f"{guess} is too low")
    elif (guess > number):
        print(f"{guess} is too high")

print("you got it!")

