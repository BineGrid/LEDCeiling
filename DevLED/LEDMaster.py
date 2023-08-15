#import LEDMatrix

#ceiling = LEDMatrix(5, 20)


def command_processor(command, arguments):
    if command == "print":
        print("Arguments for 'print':", arguments)
    elif command == "multiply":
        try:
            num = float(arguments)
            result = num * 2
            print("Result of multiplying by 2:", result)
        except ValueError:
            print("Invalid argument for 'multiply':", arguments)
    elif command == "length":
        length = len(arguments)
        print("Length of argument:", length)
    else:
        print("Unknown command:", command)


user_input = input("Enter command: ")
# Read the first five characters and convert to lowercase
command = user_input[:5].lower()
# Extract the remaining input and remove leading/trailing spaces
arguments = user_input[5:].strip()

command_processor(command, arguments)
