#FIRST you must upload the firmata examples onto the arduino using the IDE.
#This program relies on the serial connection. you cannot run the serial monitor from the IDE in parallel.
#once stopped the arduino will stop (and continue listening).
import pyfirmata as fir
import time

a = fir.Arduino('COM5')

#this example would blink the internal led
while True:
    a.digital[13].write(1)
    time.sleep(1)
    a.digital[13].write(0)
    time.sleep(0.5)
