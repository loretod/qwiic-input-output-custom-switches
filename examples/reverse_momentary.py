# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
# Demo of reading GPIO's status in TCA9534 bus-expander and an output pin change- Used for momentary switch access assistive technology
#
# SPDX-License-Identifier: MIT

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time
import neopixel
import community_tca9534

# Create I2C bus. Note: This project uses a QTPY board- other boards may require SCL and SDA pins instead
i2c = busio.I2C(board.SCL1, board.SDA1)

# Create bus-expander instances.
inputBoard = community_tca9534.TCA9534(i2c)
outputBoard = community_tca9534.TCA9534(i2c,address=0x26)

#create pixel instance
pixel = neopixel.NeoPixel(board.NEOPIXEL,1)

# Create pixel colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
OFF = (0,0,0)

# Create variables to store states of Switch 1 states
switch1 = inputBoard.get_gpio(0)
switch1_prev_state = inputBoard.get_gpio(0)

# Create variables to store states of Switch 2
switch2 = inputBoard.get_gpio(1)
switch2_prev_state = inputBoard.get_gpio(1)

# Start with both outputs in the off state
output1 = outputBoard.set_gpio(0,0)
output2 = outputBoard.set_gpio(1,0)

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

    # If switch 1/P0 is released => output 1/P0 turns on
    if switch1 != switch1_prev_state:
        if not switch1:
            output1 = outputBoard.set_gpio(0,1)
            print("Output 1 status: {0}".format(output1_status))
            pixel.fill(OFF)
        else:
            pixel.fill(BLUE)
            output1 = outputBoard.set_gpio(0,1)
            print("Output 1 status: {0}".format(output1_status))
            # Customize how long the switch will remain active. Current is 1 second
            time.sleep(1)
            output1 = outputBoard.set_gpio(0,0)
    switch1_prev_state = switch1

    # If switch 2/P1 is released => output 2/P1 turns on
    if switch2 != switch2_prev_state:
        if not switch2:
            output2 = outputBoard.set_gpio(1,1)
            print("Output 2 status: {0}".format(output2_status))
            pixel.fill(OFF)
        else:
            pixel.fill(GREEN)
            output2 = outputBoard.set_gpio(1,1)
            print("Output 2 status: {0}".format(output1_status))
            # Customize how long the switch will remain active. Current is 1 second
            time.sleep(1)
            output2 = outputBoard.set_gpio(1,0)
    switch2_prev_state = switch2

    pixel.fill(OFF)
