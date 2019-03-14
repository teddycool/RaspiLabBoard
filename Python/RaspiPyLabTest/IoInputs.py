__author__ = 'teddycool'

#Handles io-inputs from  buttons and switches

config = {"Button": {"Pressed": 0.5, "LongPressed": 3}}
import time


#The button is 'on' when holded pressed and IO defined in init is connected to ground
#Types of signals/states: released, pressed and long-pressed, times for holding are defined in config
class PushButton(object):
    def __init__(self, GPIO, inputpin):
        self._gpio = GPIO
        self._inputpin = inputpin
        self._pressed = False
        self._lastpress = False
        self._states = ["Released","Pressed", "LongPressed"]

    def initialize(self):
        #self._gpio.setmode(self._gpio.BCM)
        self._gpio.setup(self._inputpin, self._gpio.IN, pull_up_down=self._gpio.PUD_UP)

    def update(self):
        self._state = self._states[0]
        if self._gpio.input(self._inputpin) == False: #Button pressed, PullUp is released
            self._pressed = True
            if self._lastpress != self._pressed: #First round
                self._presstime = time.time()
                self._lastpress = self._pressed
            else:
                if time.time() - self._presstime > config["Button"]["LongPressed"]:
                    self._state = self._states[2]
                else:
                    if time.time() - self._presstime > config["Button"]["Pressed"]:
                        self._state = self._states[1]
        else:
            self._pressed= False
            self._lastpress = self._pressed
        return self._state


if __name__ == '__main__':
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    switches = []
    for io in [23, 24]:  #IOs for switches
        switches.append(PushButton(GPIO, io))
    for switch in switches:
        switch.initialize()
    try:
        while True:
            s= ""
            for switch in switches:
                s = s + str(switch.update()) + " "
            print str(time.time()) + " :   " + s
            time.sleep(0.5)
    except:
        GPIO.cleanup()