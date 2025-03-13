num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation: ")
if operation == '+':
    result = int(num1) + int(num2)
elif operation == '-':
    result = int(num1) - int(num2)
elif operation == '*':
    result = int(num1) * int(num2)
elif operation == '/':
    result = int(num1) / int(num2)
else:
    result = "Invalid operation"

print(num1, operation, num2 + " = ", result )
