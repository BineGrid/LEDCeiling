import random
from LEDMatrix import LEDMatrix

matrix = LEDMatrix(46, 4)

def isRGBinRange(RGBArr):
    '''
        This takes in an array of color values as strings and returns
        true if they are all between 0-255 and false otherwise
    '''
    if(RGBArr):
        for value in RGBArr:
            if int(value) < 0 or int(value) > 255:
                return False
        return True


def command_processor(command, arguments):
    '''
        This function takes in str for all its parameters
        It take in a command and then any arguments that, the
        command requires as an array of strings
        Each argument should have its own index in the array

        Ex: command_processor("fill", ["100", "100", "100"])
    '''
    try:
        if command == "help":
            print("Available Commands Are:")
            print("Clear             - (Turns all the LEDs off)")
            print("Bright val        - (Sets the brightness percentage)")
            print("Fill r g b        - (Fills all the LEDs with one color)")
            print("FillC col r g b   - (Fills a specific column with one color)")
            print("FillR row r g b   - (Fills a specific row with one color)")
            print("Set row col r g b - (Sets a LED at a specfic row col to a color)")
        elif command == "clear":
            matrix.fillMatrix(0, 0, 0)
            print("Clearing LEDs!")
        elif command == "bright":
            arguments = float(arguments[0])
            if arguments <= 1.0 and arguments >= 0.0:
                matrix.setBrightness(arguments)
                print("Brightness set to: ", arguments*100, "%", sep="")
            else:
                print("Brightness values should be between 0 and 1.0!!")
        elif command == "fill":
            if (isRGBinRange(arguments)):
                matrix.fillMatrix(int(arguments[0]), int(
                    arguments[1]), int(arguments[2]))
                print("Filling LEDs R=",
                    arguments[0], " G=", arguments[1], " B=", arguments[2], sep="")
            else:
                print("Color values should be between 0 and 255!!")
        elif command == "fillc":
            if (isRGBinRange(arguments[1:])):
                print("Filling Col ", arguments[0], " LEDs R=", arguments[1],
                    " G=", arguments[2], " B=", arguments[3], sep="")
                matrix.fillColumn(int(arguments[0]), int(arguments[1]), int(arguments[2]), int(arguments[3]))
            else:
                print("Color values should be between 0 and 255!!")
        elif command == "fillr":
            if (isRGBinRange(arguments[1:])):
                print("Filling Row ", arguments[0], " LEDs R=", arguments[1],
                    " G=", arguments[2], " B=", arguments[3], sep="")
                matrix.fillRow(int(arguments[0]), int(arguments[1]), int(arguments[2]), int(arguments[3]))
            else:
                print("Color values should be between 0 and 255!!")
        elif command == "set":
            if (isRGBinRange(arguments[2:])):
                matrix.setLEDbyRowCol(int(arguments[0]), int(arguments[1]), int(
                    arguments[2]), int(arguments[3]), int(arguments[4]), show=True)
                print("Setting LED Row: ", arguments[0], " Col: ", arguments[1], " to R=", arguments[2],
                    " G=", arguments[3], " B=", arguments[4], sep="")
            else:
                print("Color values should be between 0 and 255!!")
        else:
            print("\"", command, "\" is an unrecognized command", sep="")
    except: 
       print("Invalid arguments for ", command, "!", sep="")

# Command Loop to process user input
print("Running LEDMaster enter commands below\nType \"help\" to get a list of commands\nType \"quit\" to end the program\n")

while True:
    user_input = input("LEDMaster: ")
    command = ""
    
    # Splits the input into "words" 
    words = user_input.split()
    
    # Pop out the first "word" aka the command
    try:
        command = words.pop(0).lower()
    except:
        pass
        
    # The arguments are the "words" that remain in the arr
    arguments = words

    if command != "quit":
        command_processor(command, arguments)
    else:
        break