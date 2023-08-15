import neopixel
import time
import board

class LEDMatrix:
    
    def __init__(self, rows, cols, brightness=0.5, holes=[]):
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
            pixel_pin, self.numLEDs, self.brightness, auto_write=False, pixel_order=ORDER
        )
        
        
    def getNumLEDs(self) -> int:
        return self.numLEDs
    
    def getNumRows(self) -> int:
        return self.LEDRows
    
    def getNumColumns(self) -> int:
        return self.LEDCols
    
    def setBrightness(self, level):
        self.pixels.brightness(level)
        self.pixels.show()


    def fillMatrix(self, red:int, green:int, blue:int):
        '''`
            This will fill all the LEDs with the same color

            Args: color values between 0 - 255
        '''
        
        self.pixels.fill(red, green, blue)
        self.pixels.show()
        
    def fillColumn(self, col, red, green, blue):
        '''
            This will fill an entire col of the LEDs with 
            the same color

            Col: starts counting from zero
            Args: color values between 0 - 255
        '''

        for i in range(self.LEDRows):
            if (i + (self.LEDRows * col)) not in self.holes:
                self.pixels[i + (self.LEDCols * col)] =  (red, green, blue)