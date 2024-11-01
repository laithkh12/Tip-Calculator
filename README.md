# 💰 Tip Calculator

Welcome to the **Tip Calculator**! This simple program helps you calculate how much each person needs to pay when splitting a bill, including a tip. Just enter the total bill amount, the desired tip percentage, and the number of people sharing the bill, and it will give you the final amount each person owes.

---

## 📋 Features

- **Input for Total Bill**: Enter the total amount of the bill.
- **Tip Percentage Selection**: Choose how much tip to give (10%, 12%, or 15%).
- **Split Bill Calculation**: Enter the number of people sharing the bill to get the amount each person pays.

---

## 🔍 Code Overview

The code takes user inputs for the total bill, tip percentage, and number of people splitting the bill. It calculates the tip amount, the total bill with the tip included, and finally, the amount each person has to pay.

### Code Snippet

```python
print("Welcome to Tip Calculator!")
totalBill = float(input("What was the total bill?\n$ "))
tipPercentage = int(input("What percentage tip would you like to give 10, 12, or 15?\n$ "))
peopleNumber = int(input("How many people to split the bill?\n"))

tipPer = tipPercentage / 100
tipAmount = totalBill * tipPer
totalBillWithTip = totalBill + tipAmount

finalBillPerPerson = totalBillWithTip / peopleNumber

print(f'The bill for each person is: {round(finalBillPerPerson, 2)}')
```

## 📋 Usage Instructions
1. Clone the Repository:
```bash
git clone https://github.com/your-username/tip-calculator
cd tip-calculator
```
2. Run the Calculator: Execute the script in a Python environment:
```bash
python tip_calculator.py
```
3. Follow the Prompts:
  - Enter the total bill amount.
  - Choose a tip percentage (10, 12, or 15).
  - Enter the number of people sharing the bill.
  - The program will display the amount each person needs to pay.

## 🎮 Example Output
```bash
Welcome to Tip Calculator!
What was the total bill?
$ 150
What percentage tip would you like to give 10, 12, or 15?
$ 15
How many people to split the bill?
3
The bill for each person is: 57.5
```

## ⚙️ Customization
  Feel free to modify the code to include:
    - More tip percentage options.
    - Additional functionalities like rounding up the total amount.
    - A user interface for a more interactive experience.

## 📜 License
  This project is licensed under the MIT License. See the LICENSE file for details.

Happy calculating! 💸✨
    
