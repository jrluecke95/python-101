bill = float(input("What is the total bill amount? "))
quality = input("Level of service (good, fair, or bad)? ").lower()
split = int(input("How many people do you want to split it between?"))

quality_num = 0
if quality == "good":
    quality_num = .2
elif quality == "fair":
    quality_num = .15
else:
    quality_num = .1

tip = bill * quality_num
total = bill + tip
print("Tip Amont: $%.2f" %tip)
print("Total Amount: $%.2f" %total)
print("Amount per person $%.2f" %(total / split))

