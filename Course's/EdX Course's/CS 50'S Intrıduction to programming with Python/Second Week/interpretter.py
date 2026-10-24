expression = input("Enter an expression (e.g., 3 + 4): ")

x, operator, z = expression.split(" ")

if operator == "+":
    result = int(x) + int(z)
elif operator == "-":
    result = int(x) - int(z)
elif operator == "*":
    result = int(x) * int(z)
elif operator == "/":
    result = int(x) / int(z)

print(f"{result:.1f}")