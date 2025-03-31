num1 = float(input("input number1: "))
num2 = float(input("input number2: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("ERROR")
        exit()
else:
    print("Invalid operation")
    exit()

print(f"{num1} {operation} {num2} = {result}")
