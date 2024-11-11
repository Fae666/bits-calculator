def numcheck(question):
    error = "Please enter a number more than zero"

    while True:

        try:
            # ask user to enter a number
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


while True:
    # Ask user for width and height, must be a number more than zero
    width = numcheck("Width: ")
    height = numcheck("Height: ")

    # calculate area and perimeter
    area = height * width
    perimeter = (width + height) * 2

    # output results
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    # Exit the program if the user does not push <enter>
    again = input("Again? ")
    if again != "":
        break
    print()

print("Thank You for using RSD Area/Perimeter Calculater")