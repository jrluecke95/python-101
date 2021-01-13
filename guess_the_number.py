import random

print("I am thinking of a number")
number = random.randint(1, 10)
num_of_guesses = 5

while (num_of_guesses > 0):
    guess = int(input("What is your guess? "))
    num_of_guesses -= 1
    if (guess < number):
        print(f"{guess} is too low")
    elif (guess > number):
        print(f"{guess} is too high")
    else:
        print(f"{guess} is right! good job!")
        answer = input("would you like to play again? Y/N ").upper()
        if answer == "Y":
            num_of_guesses = 5
            number = random.randint(1, 10)
        else:
            print("Bye")
            break
    print(f"you have {num_of_guesses} guesses left")
    if num_of_guesses == 0:
        print("sorry, you didn't get it right.")
        answer = input("would you like to play again? Y/N ").upper()
        if answer == "Y":
            num_of_guesses = 5
            number = random.randint(1, 10)
        else:
            print("Bye")
            break



