import os

# Jenkins passes parameters as environment variables
num1 = float(os.getenv('NUMBER1', 0))
num2 = float(os.getenv('NUMBER2', 0))
operation = os.getenv('OPERATION', 'add')

if operation == 'add':
    result = num1 + num2
    symbol = "+"
elif operation == 'subtract':
    result = num1 - num2
    symbol = "-"
elif operation == 'multiply':
    result = num1 * num2
    symbol = "*"
elif operation == 'divide':
    result = num1 / num2 if num2 != 0 else "Error (Div by 0)"
    symbol = "/"

print(f"--- Calculation Result ---")
print(f"{num1} {symbol} {num2} = {result}")