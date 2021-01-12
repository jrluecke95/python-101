number = int(input("What number do you want to know the factors for? "))

for i in range(number + 1):
    if i == 0:
        None
    elif number % i == 0:
        print(i)
    else: 
        None