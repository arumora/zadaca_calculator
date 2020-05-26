x = int(input("Enter the value for x: "))

y = int(input("Enter the value for y: "))

operation = input("Choose operation +, -, *, or /  :")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("You did not choose potentiate math operation.")