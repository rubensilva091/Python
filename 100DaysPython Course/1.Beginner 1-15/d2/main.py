bill =  float(input("Welcome to the tip calculator.\nWhat was the total bill? €"))
tipPercentage=float(input("What percentage tipo would you like to give? "))
splitBill = float(input("How many people to split the bill? "))
final =(bill*(1+tipPercentage/100)/splitBill)
print("Each person should pay: €"+str(round(final,3)))