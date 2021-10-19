while True:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("You can only input numbers.")
    else:
        sum = num1 + num2
        print(f"The result is {sum}.")
        