import math

def show_menu():
    print("\n" + "=" * 40)
    print("      SCIENTIFIC CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Logarithm (base 10)")
    print("12. Natural Log (ln)")
    print("13. Exit")
    print("=" * 40)

while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-13): "))

        if choice == 13:
            print("Thank you for using the calculator!")
            break

        elif choice in [1, 2, 3, 4, 5]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result =", a + b)

            elif choice == 2:
                print("Result =", a - b)

            elif choice == 3:
                print("Result =", a * b)

            elif choice == 4:
                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result =", a / b)

            elif choice == 5:
                print("Result =", a ** b)

        elif choice == 6:
            n = float(input("Enter a number: "))
            if n < 0:
                print("Error: Square root of negative number not possible.")
            else:
                print("Result =", math.sqrt(n))

        elif choice == 7:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Error: Factorial not defined.")
            else:
                print("Result =", math.factorial(n))

        elif choice == 8:
            angle = float(input("Enter angle in degrees: "))
            print("Result =", math.sin(math.radians(angle)))

        elif choice == 9:
            angle = float(input("Enter angle in degrees: "))
            print("Result =", math.cos(math.radians(angle)))

        elif choice == 10:
            angle = float(input("Enter angle in degrees: "))
            print("Result =", math.tan(math.radians(angle)))

        elif choice == 11:
            n = float(input("Enter a positive number: "))
            if n <= 0:
                print("Error: Log undefined.")
            else:
                print("Result =", math.log10(n))

        elif choice == 12:
            n = float(input("Enter a positive number: "))
            if n <= 0:
                print("Error: Natural log undefined.")
            else:
                print("Result =", math.log(n))

        else:
            print("Invalid choice. Please select between 1 and 13.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
