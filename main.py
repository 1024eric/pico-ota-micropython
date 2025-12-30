
from machine import Pin
import time
# This from Github
#main code here
TIME_MS=1000
LED = Pin("LED", Pin.OUT)
while True:
    LED.off()
    time.sleep_ms(TIME_MS)
    LED.on()
    time.sleep_ms(TIME_MS)
