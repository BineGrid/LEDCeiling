#import LEDMatrix

#ceiling = LEDMatrix(5, 20)


def command_processor(command, arguments):
    if command == "help":
        print("Available Commands Are:")
        print("Clear      - (Turns all the LEDs off)")
        print("Fill r g b - (Fills all the LEDs with one color)")
    else:
        print("\"", command, "\" is an unrecognized command", sep="")


# Command Loop to process user input
command = ""
print("Running LEDMaster enter commands below\ntype \"help\" to get a list of commands\nType \"quit\" to end the program\n")

while command != "quit":
    user_input = input("LEDMaster: ")
    
    # Splits the input into "words" 
    words = user_input.split()
    
    # Pop out the first "word" aka the command
    command = words.pop(0).lower()
    
    # The arguments are the "words" that remain in the arr
    arguments = words

    command_processor(command, arguments)
