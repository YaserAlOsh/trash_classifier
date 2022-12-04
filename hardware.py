import time
from gpiozero import LED

class LEDs:
    def __init__(self):       
        self.red = LED(5)
        self.blue = LED(26)
        self.yellow = LED(6)
        self.green = LED(13)
    
    def general_led(self):
        self.blue.on()
        time.sleep(2)
        self.blue.off()
    
    def metaL_led(self):
        self.red.on()
        time.sleep(2)
        self.red.off()
    
    def paper_led(self):
        self.yellow.on()
        time.sleep(2)
        self.yellow.off()
        
    def plastic_led(self):
        self.green.on()
        time.sleep(2)
        self.green.off()
