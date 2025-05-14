# Discount Calculator

price = float(input("Enter product price: "))

if price > 1000:
    discount = price * 0.10
else:
    discount = price * 0.05

print("Discount:", discount)
print("final price:", price - discount)