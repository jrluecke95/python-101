coins = 0
print("you have %i coins" %coins)

while coins > -1:
    answer = (input("Do you want another? ")).lower()
    if answer == "yes":
        coins += 1
        print("you have %i coins" %coins)
    else:
        print("Bye")
        break