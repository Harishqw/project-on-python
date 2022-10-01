# creating while loop
while True:
    # printing the available options
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    # asking user to Enter his choice
    choice = int(input("Enter your choice: "))
    # checking the choice between 1 and 4
    if (choice>=1 and choice<=4):
        # asking to enter two options
        print("Enter two numbers: ")
        # accepting first number
        num1 = int(input())
        # accepting second number
        num2 = int(input())
        # checking if number is 1
        if choice == 1:
            # adding
            res = num1 + num2
            # printing Addition
            print("Result = ", res)
        # checking if number is 2
        elif choice == 2:
            # Subtracting
            res = num1 - num2
            # printing Subtraction
            print("Result = ", res)
        # checking if number is 3
        elif choice == 3:
            # Multiplication
            res = num1 * num2
            # printing Result
            print("Result = ", res)
        # after checking all 3 choice,
        # only one operation left, i.e. for Division
        else:
            # Division
            res = num1 / num2
            # printing Result
            print("Result = ", res)
    # checking if the choice is 5
    elif choice == 5:
        # if choice is 5, we will exit the program
        exit()
    # everything, except the five choices is useless
    # so, we will print Wrong input..!!
    else:
        print("Wrong input")
