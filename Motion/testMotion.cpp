#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev()
spi.open(2, 0)
spi.max_speed_hz = 5000000

# Split an integer input into a two byte array to send via SPI
def write_ICM20948(input):
    spi.xfer(input)

def read_ICM20948(reg, numbytes):
    reg = reg | 0x80
    data = [0xFF] * (numbytes + 1)
    data[0] = reg
    print (*data)
    spi.xfer(data)
    print (*data)

# Repeatedly switch a MCP4151 digital pot off then on
while True:
    read_ICM20948(0x00,1)
    time.sleep(1)