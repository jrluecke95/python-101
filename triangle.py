height = int(input("How tall do you want your triangle to be? "))
def bottom_calc(height):
    x = 1
    for x in range(height):
        x += 2
        print(x)
    return x

bottom = bottom_calc(height)
print(bottom)