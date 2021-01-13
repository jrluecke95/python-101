height = int(input("How tall do you want your triangle to be? "))
def bottom_calc(height):
    bot = 1
    # having height -1 gets rid of extra spacing on bottom row
    # with height at normal range it adds an extra space on either side on teh bottom row
    for x in range(height - 1):
        bot += 2
        #print(x)
    return bot

bottom = bottom_calc(height)
row = 1

# keep this height at normal value because range doesnt inclue ending index
# otherwise it won't count everything as the last index gets chopped off
for i in range(height):
    spacing = int((bottom - row) / 2)
    print((" " * spacing) + "*" * row + (" " * spacing))
    row += 2