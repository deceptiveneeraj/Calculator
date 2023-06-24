import math

print("Hello There, I am Neeraj.")
print("Welcome to the Scientific Calculator!")

while True:
    print("\nPlease select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Exponent")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Table")
    print("0. Quit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 + num2)
    elif choice == 2:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 - num2)
    elif choice == 3:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result: ", num1 * num2)
    elif choice == 4:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print("Result: ", num1 / num2)
    elif choice == 5:
        num = float(input("\nEnter a number: "))
        print("Result: ", num * num)
    elif choice == 6:
        num = float(input("\nEnter a number: "))
        print("Result: ", math.sqrt(num))
    elif choice == 7:
        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter an exponent: "))
        print("Result: ", num1 ** num2)
    elif choice == 8:
        num = float(input("\nEnter a number: "))
        print("Result: ", math.sin(num))
    elif choice == 9:
        num = float(input("\nEnter a number: "))
        print("Result: ", math.cos(num))
    elif choice == 10:
        num = float(input("\nEnter a number: "))
        print("Result: ", math.tan(num))
    elif choice == 11:
        num = int(input("Display multiplication table of? "))
        for i in range(1, 11):
            print(num, 'x', i, '=', num * i)
    elif choice == 0:
        print("Thank you for using the Scientific Calculator!")
        break
    else:
        print("Invalid choice. Please try again.")
