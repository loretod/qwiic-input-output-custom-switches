# qwiic-input-output-custom-switches
A collection of circuitpython programs working with Milador's qwiic plug and play boards for customization of input switch behaviors.

There are 3 example files in order to customize the behavior of an access switch activation

##Momentary
Input press results in output activation. User may customize the length of time the output remains active.

Image:
![USB cable connected to a controller with a custom board connected via grove wire with AT switch. Followed by another custom board with a wire connected to an adapted toy. Hand presses the switch and toy activated for 1 second](/images/momentary_demo.gif "Momentary Switch Setting Demo")

##Reverse Momentary
Input remains pressed. Activation occurs when the switch is released. Length of activation may be customized for user preference.

Image:
![USB cable connected to a controller with a custom board connected via grove wire with AT switch. Followed by another custom board with a wire connected to an adapted toy. Hand releases the switch and toy activated for 1 second](/images/reverse_demo.gif "Momentary Switch Setting Demo")

##Latch System
Input press turn on and leave on the output until the switch is pressed again.

Image:
![USB cable connected to a controller with a custom board connected via grove wire with AT switch. Followed by another custom board with a wire connected to an adapted toy. Hand presses the switch and the toy activated. Hand presses the switch again and toy is deactivated](/images/latch_demo.gif "Latch Switch Setting Demo")
