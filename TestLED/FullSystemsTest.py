import time
import board
import neopixel

# PWM Pin connected to the LED's
pixel_pin = board.D12

# The number of NeoPixels in total
num_pixels = 600

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

def individualColorTest(wait: float, testRed = True, testBlue = True, 
                        testGreen = True, testWhite = True):
    for i in range(num_pixels):
        if(testRed):
            pixels[i] = (255, 0, 0)
            pixels.show()
            time.sleep(wait/3)
            
        if(testBlue):
            pixels[i] = (0, 255, 0)
            pixels.show()
            time.sleep(wait/3)
        
        if(testGreen):
            pixels[i] = (0, 0, 255)
            pixels.show()
            time.sleep(wait/3)
            
        if(testWhite):
            pixels[i] = (255, 255, 255)
            pixels.show()
            time.sleep(wait)
        
    

