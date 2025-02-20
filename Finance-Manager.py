salary = float(input("Enter your salary of the month: "))
month = input("Enter the month: ")

savings_percent = float(input("Enter the percentage of salary allocated to savings: "))
rent_percent = float(input("Enter the percentage of salary allocated to rent: "))
electrecity_percent = float(input("Enter the percentage of salary allocated to electrecity: "))

#calculating
savings = (savings_percent/100) * salary
rent = (rent_percent/100) * salary
electrecity = (electrecity_percent/100) * salary

total_expense = savings + rent + electrecity
remainder = salary - total_expense

yearly_rent = rent * 12
yearly_electrecity = electrecity * 12

salary_squared = salary ** 2

additional_saving = 50
percent_additional_saving =  additional_saving / savings


print(salary)
print(month)
print(savings_percent)
print(rent_percent)
print(electrecity_percent)
print(savings)
print(rent)
print(electrecity)
print(total_expense)
print(remainder)
print(yearly_rent)
print(yearly_electrecity)
print(salary_squared)
print(percent_additional_saving)