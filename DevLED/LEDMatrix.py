import neopixel
import time
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
        pixel_pin = board.D12
        
        # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
        ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            pixel_pin, self.numLEDs, brightness=self.brightness, auto_write=False, pixel_order=ORDER
        )
        
        
    def getNumLEDs(self):
        return self.numLEDs
    
    def getNumRows(self):
        return self.LEDRows
    
    def getNumColumns(self):
        return self.LEDCols
    
    def setBrightness(self, level:float):
        self.pixels.brightness = level
        self.pixels.show()
        
    # TODO combine with numHolesBeforeLED function
    def getLEDAddress(self, row:int, col:int):
        '''
            Takes in a row and col number and returns the address
            within the pixels[] array of that LED
            
            Returns None if the LED is at a hole
        '''
        if (row, col) in self.holes:
            return None
        if col % 2 == 1:
            row = self.LEDRows - row - 1
        return (row * self.LEDCols + col)
    
    # TODO Combine this function with the getLEDAddress function
    def numHolesBeforeLED(self, row: int, col: int):
        '''
            This function takes in an LED address and tell you how
            many holes "Fake LED" are before it
            That way you can know how much to offest your new address
        '''
        numLEDs = 0
        LEDAddress = self.getLEDAddress(row, col)

        for hole in self.holes:
            if (self.getLEDAddress(hole[0], hole[1]) < LEDAddress):
                numLEDs += 1

        return numLEDs


    def fillMatrix(self, red:int, green:int, blue:int):
        '''`
            This will fill all the LEDs with the same color

            Args: color values between 0 - 255
        '''
        
        self.pixels.fill((red, blue, green))
        self.pixels.show()
    
    # TODO rewrite this to use the new getaddress function properly
    def fillColumn(self, col:int, red:int, green:int, blue:int):
        '''
            This will fill an entire col of the LEDs with 
            the same color

            Col: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDRows):
            # Calculate the correct LED address to set to emulate a "column"
            currLEDNum = self.getLEDAddress(i, col)
            
            # Check how many holes are before the LED and subtract the amount
            # from the current address to essentially skip thoughs LEDs
            holes_before = self.numHolesBeforeLED(currLEDNum)
            currLEDNum = currLEDNum - holes_before
            
            print("Setting LED: ", currLEDNum, " to R=", red,
                    " G=", green, " B=", blue, sep="")
            self.pixels[currLEDNum] = (red, blue, green)

        self.pixels.show()
    
    # TODO write this function
    def fillRow(self, row:int, red:int, green:int, blue:int):
        '''
            This will fill an entire row of the LEDs with 
            the same color

            Row: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDCols):
            currLEDNum = i + (self.LEDCols * row)


        self.pixels.show()
        
        
# TODO write the setLEDbyRowCol function

