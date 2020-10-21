a = float(input())
b = float(input())
operation = input()

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == 'pow':
    print(a ** b)
elif operation == '/':
    print((a / b) if b != 0 else "Division by 0!")
elif operation == 'mod':
    print((a % b) if b != 0 else "Division by 0!")
elif operation == 'div':
    print((a // b) if b != 0 else "Division by 0!")
