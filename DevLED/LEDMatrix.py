import neopixel
import time
import board

class LEDMatrix:
    
    def __init__(self, rows, cols, brightness=1.0, holes=[]):
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
        
    def getLEDAddress(self, row:int, col:int):
        if (row, col) in self.holes:
            return None
        if col % 2 == 1:
            col = self.LEDRows - col - 1
        return row * self.num_cols + col


    def fillMatrix(self, red:int, green:int, blue:int):
        '''`
            This will fill all the LEDs with the same color

            Args: color values between 0 - 255
        '''
        
        self.pixels.fill((red, blue, green))
        self.pixels.show()
        
    def numHolesBeforeLED(self, address:int):
        '''
            This function takes in an LED address and tell you how
            many holes "Fake LED" are before it
            That way you can know how much to offest your new address
        '''
        numLEDs = 0
        for i in range(len(self.holes)):
            if self.holes[i] < address:
                numLEDs += 1
        
        return numLEDs
    
    def fillColumn(self, col:int, red:int, green:int, blue:int):
        '''
            This will fill an entire col of the LEDs with 
            the same color

            Col: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDRows):
            # Calculate the correct LED address to set to emulate a "column"
            currLEDNum = i + (self.LEDRows * col)
            
            # Check how many holes are before the LED and subtract the amount
            # from the current address to essentially skip thoughs LEDs
            holes_before = self.numHolesBeforeLED(currLEDNum)
            currLEDNum = currLEDNum - holes_before
            
            print("Setting LED: ", currLEDNum, " to R=", red,
                    " G=", green, " B=", blue, sep="")
            self.pixels[currLEDNum] = (red, blue, green)

        self.pixels.show()
        
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
        
    def setLEDbyRowCol(self, row:int, col:int, red:int, green:int, blue:int):
        '''
            This function will take in a col and a LEDNum to determine 
            what single LED you're trying to change. Each column starts counting
            from 0. 0 starts at the LED against the back wall of the room
            This function does not automatically call show()
            
            Args: Color values between 0-255
        '''
        


