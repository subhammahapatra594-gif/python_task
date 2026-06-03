num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Answer =", num1 + num2)

elif choice == 2:
    print("Answer =", num1 - num2)

elif choice == 3:
    print("Answer =", num1 * num2)

elif choice == 4:
    print("Answer =", num1 / num2)

else:
    print("Invalid Choice")