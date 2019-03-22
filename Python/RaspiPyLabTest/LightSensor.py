__author__ = 'teddycool'
#REF: http://www.rpiblog.com/2012/11/reading-analog-values-from-digital-pins.html
#This is calibrated with a LDR GL  5516 and a 47uF elotrolytic capacitor.

import time

class LightSensor(object):

    def __init__(self,gpio,pin=14):
        self._gpio=gpio
        self._pin = pin


    def initialize(self):
        # Discharge capacitor
        self._gpio.setup(self._pin, self._gpio.OUT)
        self._gpio.output(self._pin, self._gpio.LOW)
        time.localtime(0.1)
        self._lastDischarge = time.time()
        self._count =0


    def update(self): #Non-locking meassure method used from a 'game-loop' type of program or as a separate thread
        cnt = 0
        if self._count == 0:
            self._gpio.setup(self._pin, self._gpio.IN)
            self._count = self._count + 1
        else:
            if self._gpio.input(self._pin) == self._gpio.LOW:   #still LOW, continue to count time...
                self._count = self._count + 1
            else:                                               #signal high, stop and fetch counter, reset for new meassurement cycle
                cnt = self._count + 1
                self.initialize()
        return cnt                                              #As long as cnt = 0 measure is still in progress


    def measure(self): #Locking measure method that use a timer for the coundet and return when measure is done
        cnt = 0
        while (self._gpio.input(self._pin) == self._gpio.LOW):
            cnt = self._count + 1
            time.sleep(0.1)
        return cnt



if __name__ == '__main__':
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    print "Testcode for LightSensor"
    ls=LightSensor(GPIO, 14)
    ls.initialize()

    while True:
        print "---------------------"
        print "Non-Locking measure"
        print ls.update()
        time.sleep(0.1)

        print "Locking measure"
        print ls.measure()
        print ""









