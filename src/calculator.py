

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
    
total = num1 + num2
difference = num1 - num2
product = num1 * num2
    
if num2 != 0:
        quotient = num1 / num2
        quotient_text = str(quotient)
else:
        quotient_text = "undefined (cannot divide by zero)"
    
print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient_text}")

