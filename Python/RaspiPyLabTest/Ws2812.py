__author__ = 'teddycool'

#This code depend on https://github.com/rpi-ws281x/rpi-ws281x-python Install this first.

import time
from rpi_ws281x import *

LED_COUNT = 3
LED_PIN = 18
LED_FREQ_HZ= 800000
LED_DMA= 10
LED_BRIGHTNESS= 100
LED_INVERT= False


class Ws2812(object):

    def __init__(self):
       self._displayArray = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)


    def initialize(self):
        self._displayArray.begin()



    def test(self):
        print "Test started..."

        #Loop through all leds
        for i in range(LED_COUNT):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
        self._displayArray.show()
        for i in range(LED_COUNT):
            self._displayArray.setPixelColor(i, Color(0, 50, 0, ))
            self._displayArray.show()
            time.sleep(0.1)
        time.sleep(2)
        for i in range(LED_COUNT):
            self._displayArray.setPixelColor(i, Color(50, 0, 0, ))
            self._displayArray.show()
            time.sleep(0.1)
        time.sleep(2)
        for i in range(LED_COUNT):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
            self._displayArray.show()
            time.sleep(0.1)


    def SetBrightness(self, brightness):
        self._brightness= brightness
        self._displayArray.setBrightness(brightness)

    def ToggleBrightness(self):
        if self._brightness < 100:
            self._brightness = self._brightness + 10
        else:
            self._brightness= 10
        self.SetBrightness(self._brightness)
        print "Brigthness = " + str(self._brightness)



    def off(self):
        #Turn off the display...
        for i in range(LED_COUNT):
            self._displayArray.setPixelColor(i, Color(0, 0, 0, ))
        self._displayArray.show()



if __name__ == '__main__':
    print "Testcode for Ws2812"
    bd= Ws2812()
    bd.initialize()
    bd.test()
    while(1):
        bd.test()
        time.sleep(1)
