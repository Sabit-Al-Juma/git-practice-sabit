from datetime import date
from utils import add, subtract,multiply,divide

print("Name : Sabit Al Juma")
Date= date.today()
print(f"Today's Date: {Date}")

Addition = add(10, 5)
print(f"Add: {Addition}")
Subtraction = subtract(10, 5)
print(f"Subtract: {Subtraction}")

Multiplication = multiply(10, 5)
print(f"Multiply: {Multiplication}")

print("Divide 1:", divide(5, 0))
print("Divide 2:", divide(10, 2))