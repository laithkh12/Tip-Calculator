print("Welcome to Tip Calculator!")
totalBill = float(input("What was the total bill?\n$ "))
tipPercentage = int(input("What percentage tip would you like to give 10 12 15?\n$ "))
peopleNumber = int(input("How many people to split the bill?\n"))

tipPer = tipPercentage / 100
tipAmount = totalBill * tipPer
totalBillWithTip = totalBill + tipAmount

finalBillPerPerson = totalBillWithTip / peopleNumber

print(f'The bill for each person is: {round(finalBillPerPerson, 2)}')
