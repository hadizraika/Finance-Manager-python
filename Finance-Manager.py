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

print("================ Financial Management Program ================")
print(f"This is the salary: {salary:.2f}$ for this Month: {month}")
print(f"Savings: {savings}$")
print(f"Rent: {rent:.2f}$")
print(f"Electrecity: {electrecity:.2f}$")
print(f"Total expense: {total_expense:.2f}$")
print(f"Remainder: {remainder:.2f}$")
print(f"Yearly rent: {yearly_rent:.2f}$")
print(f"Yearly electrecity: {yearly_electrecity:.2f}$")
print(f"Salary squared: {salary_squared:.2f}$")
print(f"Percent additonal savings: {percent_additional_saving}%")
print("==============================================================")