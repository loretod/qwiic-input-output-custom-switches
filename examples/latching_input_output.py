# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
# Demo of reading GPIO's status in TCA9534 bus-expander and latching an output pin- Used for switch access assistive technology
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

# Create pixel instance
pixel = neopixel.NeoPixel(board.NEOPIXEL,1)

# Create pixel colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
OFF = (0,0,0)

# Create variables to store states of Switch 1 press and latch state
switch1 = inputBoard.get_gpio(0)
switch1_prev_state = inputBoard.get_gpio(0)
switch1_latch = False

# Create variables to store states of Switch 2 press and latch state
switch2 = inputBoard.get_gpio(1)
switch2_prev_state = inputBoard.get_gpio(1)
switch2_latch = False

# Start with both outputs in the off state
output1 = outputBoard.set_gpio(0,0)
output2 = outputBoard.set_gpio(1,0)

# Main loop- sets the input and output
while True:
    # Sets instance of switches connected to P0 and P1 on the input board
    switch1 = inputBoard.get_gpio(0)
    switch2 = inputBoard.get_gpio(1)

    # Check to see if there is a differnce in variables for switch 1/P0 and begin latching sequence
    if switch1 != switch1_prev_state:
        switch1_prev_state = switch1
        if not switch1 and not switch1_latch:
            print("Switch 1 Latch Start")
            pixel.fill(BLUE)
            output1 = outputBoard.set_gpio(0,1)
            # Uncomment line below if you would like both outputs to latch when Switch 1 is pressed
            # output2 = outputBoard.set_gpio(1,1)
            switch1_prev_state = switch1
            switch1_latch = True

        elif not switch1 and switch1_latch:
            print("Switch 1 Latch Stop")
            pixel.fill((0,0,0))
            output1 = outputBoard.set_gpio(0,0)
            # Uncomment line below if you need to turn off the latch for both outputs when Switch 1 is pressed again
            #output2 = outputBoard.set_gpio(1,0)
            switch1_latch = False

    # Check to see if there is a differnce in variables for switch 2/P1 and begin latching sequence
    if switch2 != switch2_prev_state:
        switch2_prev_state = switch2
        if not switch2 and not switch2_latch:
            print("Switch 2 Latch Start")
            pixel.fill(BLUE)
            output2 = outputBoard.set_gpio(1,1)
            # Uncomment line below if you would like both outputs to latch when Switch 2 is pressed
            # output1 = outputBoard.set_gpio(0,1)
            switch2_prev_state = switch2
            switch2_latch = True

        elif not switch2 and switch2_latch:
            print("Switch 2 Latch Stop")
            pixel.fill(OFF)
            output2 = outputBoard.set_gpio(1,0)
            # Uncomment line below if you need to turn off the latch for both outputs when Switch 2 is pressed again
            #output1 = outputBoard.set_gpio(0,0)
            switch2_latch = False
