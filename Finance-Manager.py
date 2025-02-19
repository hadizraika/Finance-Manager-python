salary = float(input("Enter your salary of the month: "))
month = input("Enter the month: ")

savings_percent = float(input("Enter the percentage of salary allocated to savings: "))
rent_percent = float(input("Enter the percentage of salary allocated to rent: "))
electrecity_percent = float(input("Enter the percentage of salary allocated to electrecity: "))

#calculating
savings = (savings_percent/100) * salary
rent = (rent_percent/100) * salary
electrecity = (electrecity_percent/100) * salary

print(salary)
print(month)
print(savings_percent)
print(rent_percent)
print(electrecity_percent)
print(savings)
print(rent)
print(electrecity)