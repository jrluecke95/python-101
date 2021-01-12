height = int(input("How tall do you want your triangle to be? "))
def bottom_calc(height):
    bot = 1
    for x in range(height - 1):
        bot += 2
        print(x)
    return bot

bottom = bottom_calc(height)
print(bottom)