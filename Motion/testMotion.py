# Motion Test Python

# import spidev # Does not talk to computer, talks to linux board.. import not working
import time
import datetime
import binascii # Converting between binary and various ASCII-encoded binary representations
import os.path # Operations on pathnames
import math # Mathematical functions
import binhex # Encode and decode files in binhex4 format

spi = spidev.SpiDev()
spi.open(2, 0)
spi.maxSpeedHz = 5000000


# Split an integer input into a two byte array to send via SPI
def write_ICM20948(input):
    spi.xfer(input)

def read_ICM20948(reg, numbytes):
    reg = reg or 0x80
    data = ["0xFF", "hex"] * (numbytes + 1)
    data[0] = reg
    print(*data)

    spi.xfer(data)
    print(*data)

def main():
    # Repeatedly switch a MCP4151 digital pot off then on
  while True:
      F = open("icm20948.cpp", "r") # (0x00,1))
    # read_ICM20948(0x00,1)

  time.sleep(1)

if __name__ == '__main__': main()
