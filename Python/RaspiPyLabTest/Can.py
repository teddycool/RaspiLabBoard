#Simple class using CAN interface MCP2515 on SPI bus
#https://python-can.readthedocs.io/en/stable/index.html
#https://harrisonsand.com/can-on-the-raspberry-pi/
#pip install python-can

import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/sqlite3')



import can


class Can(object):
    def __init__(self,):
        self._bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
        #TBD...



#    def ReadMsg(self):




    def SendMsg(self, msg):
        try:
            self._bus.send(msg)
            print("Message sent on {}".format(self._bus.channel_info))
        except can.CanError:
            print("Message NOT sent")





if __name__ == '__main__':
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    myCan =Can()
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=[0, 25, 0, 1, 3, 1, 4, 1],
                      is_extended_id=True)

    myCan.SendMsg(msg)



