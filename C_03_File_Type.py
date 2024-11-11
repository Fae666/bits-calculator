#
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
