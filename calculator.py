num1 = float(input("Enter the number:"))
op = input("Enter the operater:")
num2 = float(input("Enter the number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")