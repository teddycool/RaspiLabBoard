#Simple class using CAN interface MCP2515 on SPI bus
#https://python-can.readthedocs.io/en/stable/index.html
#https://harrisonsand.com/can-on-the-raspberry-pi/
#pip install python-can


# 3073.000799 1  18FF3E30x       Rx   d 8 FF FF FF FF FF FF FF FF  Length = 0 BitCount = 0 ID = 419380784x
# 3073.001423 1  CFF7427x        Rx   d 8 FC FF F4 00 3F FF FF FF  Length = 0 BitCount = 0 ID = 218068007x
# 3073.001458 2  CFF3127x        Rx   d 8 00 C0 00 C0 FF FF FF FF  Length = 0 BitCount = 0 ID = 218050855x
# 3073.001488 6  4F0090Bx        Rx   d 8 FF FF FF 8F 7D D7 7D 7E  Length = 0 BitCount = 0 ID = 82839819x
# 3073.001558 4  18FF3B27x       Rx   d 8 CC CC CC FF CC FF FF FF  Length = 0 BitCount = 0 ID = 419380007x
# 3073.001705 1  CF02F11x        Rx   d 8 F1 FF FA FF FF FF FF FF  Length = 0 BitCount = 0 ID = 217067281x


import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/sqlite3')



import can


class Can(object):
    def __init__(self,):
        self._bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
        #TBD...



    def ReadMsg(self,bus):
        for msg in bus:
            print(msg)



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




