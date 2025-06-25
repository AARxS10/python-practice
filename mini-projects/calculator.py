# A calculator
# Abdul Ahad Rahman
# 2025/06/26

print("Heyy 👋 Welcome to my calculator!")

a = float(input("Enter your first number:\n"))
b = float(input("Enter your second number:\n"))

print("\nWhat do you want to do? Type the number of the operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

mode = input("\nEnter your choice (1/2/3/4): ")

if mode == '1':
    print("Your answer is:", a + b)
elif mode == '2':
    print("Your answer is:", a - b)
elif mode == '3':
    print("Your answer is:", a * b)
elif mode == '4':
    if b == 0:
        print("Cannot divide by zero — undefined.")
    else:
        print("Your answer is:", a / b)
else:
    print("Invalid choice. Please choose 1, 2, 3, or 4.")
