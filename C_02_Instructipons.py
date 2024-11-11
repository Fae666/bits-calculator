# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays Instructions
def Instructions():
    print("Instructions go here....")
    statement_generator("Instructions", "*")

    print('''
Instructions go here.
- Instructions 1 
- Instructions 2
- ect.
    ''')

# Main routine goes here
want_instructions = input("Press <enter> to read the Instructions"
                          "or press any key to continue")
# Display Instructions if requested
if want_instructions == "":
    Instructions()
    print("program continues")

def get_filetype():
    while True:
        response = input("File Type: ").lower()

        #
        if response == "xxx" or response == "i" or response == "3x":
            return response

        #
        elif response in ['integer', 'int']:
            return "integer"

        #
        elif response in ['image', 'picture', 'img', 'p', 'pic']:
            return "image"

        #
        elif response in ["text", 'txt', 't']:
            return "text"

        #
        else:
            print("Please enter a valid file type")


#
while True:
    file_type = get_filetype()


    #
    if file_type == "i":

        want_image = input("press <enter> for an integer or any key for image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You Choose {file_type}")

    if file_type == "xxx" or file_type == "3x":
        break


