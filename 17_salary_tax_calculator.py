# Salary Tax Calculator

salary = float(input("Enter your salary: "))

if salary <= 25000:
    tax = 0
elif salary <= 50000:
    tax = salary * 0.10
else:
    tax = salary * 0.20

print("Tax to pay:",tax)