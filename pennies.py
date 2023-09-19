pennies = int (input("Your number of pennies: "))
dollars = pennies // 100
pennies %= 100
quarters = pennies // 25
pennies %= 25
dimes = pennies // 10
pennies %= 10
nickels = pennies // 5
pennies %= 5
pennies_left = pennies
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies_left)

