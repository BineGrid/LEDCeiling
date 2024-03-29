import neopixel
import board

class LEDMatrix:
    def __init__(self, rows:int, cols:int, brightness=1.0, holes=[]):
        '''
            Enter in the number of rows and columns in your system as int's
            
            The brightness is defaulted to max, because you can also control
            the brightness by just using the 0-255 color values, the brightness 
            value just scales those 0-255 values
            
            For the holes, enter in an array of tuples like so holes=[(row, col), (row, col)...]
            A hole is somewhere we expect there to be an LED, but for whatever reason we
            can't put one there, thus we add a hole that way the strips all stay properly
            aligned. Making displaying images and patterns look proper as if tho's LEDs where there
        '''
        self.LEDRows = rows
        self.LEDCols = cols
        self.brightness = brightness
        self.holes = holes 
        
        # Calculate the total number of LEDs thats within the matrix
        self.numLEDs = (self.LEDRows * self.LEDCols) - len(self.holes)
        
        # Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
        # NeoPixels must be connected to D10, D12, D18 or D21 to work.
        pixelPin = board.D12
        
        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            pixelPin, self.numLEDs, brightness=self.brightness, auto_write=False, pixel_order=ORDER
        )
    
    def getNeoPixelObj(self):
        '''
            The Neopixel LED Object
            You can access the Lib directly through this object
            Becareful!
        '''
        return self.pixels
    
    def getNumLEDs(self):
        return self.numLEDs
    
    def getNumRows(self):
        return self.LEDRows
    
    def getNumColumns(self):
        return self.LEDCols
    
    def setBrightness(self, level:float):
        self.pixels.brightness = level
        self.pixels.show()

    def getLEDAddress(self, row: int, col: int):
        """
            This function takes a row and column value and returns the address within the 1D pixels[] array.
            It adjusts the address automatically to account for any holes in the system.
            It returns None if the specified LED is at a hole.
        """
        # Check if the specified LED is at a hole
        if (row, col) in self.holes:
            return None

        # Initialize the variable to keep track of the adjusted LED holes
        adjLEDHoles = 0

        # Iterate through each hole to calculate adjusted LED holes
        for hole in self.holes:
            if hole[1] < col or (hole[1] == col and hole[0] <= row):
                adjLEDHoles += 1

        # Calculate the total number of LEDs in the matrix
        totalLEDs = self.getNumLEDs()

        # Calculate the 1D address without considering adjusted holes
        baseAddress = col * self.LEDRows + row

        # Adjust the address by subtracting the count of holes before the specified LED
        adjAddress = baseAddress - adjLEDHoles

        # Ensure that the adjusted address stays within the range [0, total_leds)
        adjAddress = max(0, min(adjAddress, totalLEDs - 1))

        # Adjust the address for odd columns
        if col % 2 == 1:
            adjAddress = (self.LEDRows - (adjAddress %
                        self.LEDRows)) + (col * self.LEDRows) - 1

        return adjAddress

    def setLEDbyAddress(self, address: int, red: int, green: int, blue: int, show=False):
        '''
            Sets a single specific LED to a r g b value given a row and col
            rgb values must be between 0 - 255
            This doesn't take holes into account!!
        '''
        try:
            self.pixels[address] = (red, blue, green)
            print("Setting LED: ", address, " to R=", red,
                    " G=", green, " B=", blue, sep="")
        except:
           print("LED Address: ", address, " Out of Bounds!!", sep="")
        
        if show:
            self.pixels.show()
        
    def setLEDbyRowCol(self, row: int, col: int, red: int, green: int, blue: int, show=False):
        '''
            Sets a single specific LED to a r g b value given a row and col
            
            rgb values must be between 0 - 255
        '''
        address = self.getLEDAddress(row, col)
        
        if address is None:
            return
        
        self.setLEDbyAddress(address, red, green, blue, show)
        
    def fillMatrix(self, red:int, green:int, blue:int):
        '''`
            This will fill all the LEDs with the same color

            Args: color values between 0 - 255
        '''
        
        self.pixels.fill((red, blue, green))
        self.pixels.show()
    
    def fillColumn(self, col:int, red:int, green:int, blue:int):
        '''
            This will fill an entire col of the LEDs with 
            the same color

            Col: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDRows):
            self.setLEDbyRowCol(i, col, red, green, blue)
   
        self.pixels.show()

    def fillRow(self, row:int, red:int, green:int, blue:int):
        '''
            This will fill an entire eow of the LEDs with 
            the same color

            Col: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDCols):
            self.setLEDbyRowCol(row, i, red, green, blue)

        self.pixels.show()