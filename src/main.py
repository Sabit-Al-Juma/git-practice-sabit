from datetime import date
from utils import add, subtract,multiply

print("Name : Sabit Al Juma")
Date= date.today()
print(f"Today's Date: {Date}")

Addition = add(10, 5)
print(f"Add: {Addition}")
Subtraction = subtract(10, 5)
print(f"Subtract: {Subtraction}")

Multiplication = multiply(10, 5)
print(f"Multiply: {Multiplication}")