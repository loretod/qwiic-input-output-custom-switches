# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
# Demo of reading GPIO's status in TCA9534 bus-expander and an output pin change- Used for switch access assistive technology
#
# SPDX-License-Identifier: MIT

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time
import neopixel
import community_tca9534

# Create I2C bus.
i2c = busio.I2C(board.SCL1, board.SDA1)

# Create bus-expander instance.
inputBoard = community_tca9534.TCA9534(i2c)
outputBoard = community_tca9534.TCA9534(i2c,address=0x26)

#create pixel instance
pixel = neopixel.NeoPixel(board.NEOPIXEL,1)

# Create pixel colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
OFF = (0,0,0)

# Main loop:
while True:
    # Sets instance of switches connected to P0 and P1 on the input board
    switch1 = inputBoard.get_gpio(0)
    switch2 = inputBoard.get_gpio(1)

    # Sets instance of output connected to P0 and P1 on the output
    output1 = outputBoard.set_gpio(0,0)
    output2 = outputBoard.set_gpio(1,0)

    # Get status of outputs for debug purposes
    output1_status = outputBoard.get_gpio(0)
    output2_status = outputBoard.get_gpio(1)

    # If switch 1/P0 is pressed => output 1/P0 turns on
    if not switch1:
        pixel.fill(GREEN)
        print('Switch 1 pressed')
        output1 = outputBoard.set_gpio(0,1)
        print("Output 1 status: {0}".format(output1_status))

    # If switch 2/P1 is pressed => output 2/P1 turns on
    if not switch2:
        pixel.fill(BLUE)
        print('Switch 2 pressed')
        output2 = outputBoard.set_gpio(1,1)
        print("Output 2 status: {0}".format(output2_status))

    # Delay for .2 seconds -- change the value in the parentheses to lengthen the amount of time the output remains on.
    time.sleep(0.2)
    pixel.fill(OFF)
