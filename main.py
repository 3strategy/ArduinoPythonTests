# FIRST you must upload the firmata example onto the arduino using the Arduino IDE.
import pyfirmata
import time

a = pyfirmata.Arduino('COM5')

pin=a.get_pin('d:13:o')  # here setting pin to be digital number 13, and setting it as OUTPUT.
servo=a.get_pin('d:9:s')  # this will set pin 9 to be used as a servo

#this controls the servo (servo is set to a designated position (usually between 0 to 180 or a bit less).
def serpos(ser,pos,sleep=1):
    ser.write(pos)
    pin.write(1)
    print(pos)
    time.sleep(0.2)
    pin.write(0)
    time.sleep(sleep) # need to give the servo a bit more time...

k=1
serpos(servo, 60)

while True:  # main arduino loop
    print('start of loop', k)
    serpos(servo,130)
    serpos(servo,60)
    serpos(servo,15)
    serpos(servo,60,6)  # sleeping 6 seconds
    k+=1






