width = int(input("What width do you want for the box? "))
height = int(input("What height do you want for the box? "))

x = 0

for x in range(width):
    if x == 0:
        print("*" * width)
    elif 0 < x < (width - 1):
        print("*" + " " * (width - 2) + "*")
    else:
        print("*" * width)