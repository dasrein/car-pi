# car-pi
Configuration settings needed by the 5 inch DSI touch screen: https://www.waveshare.com/wiki/5inch_DSI_LCD

The speakers are driven by a Hifiberry Amp2 (1.1) and some modifications to the pi config file are necessary for the correct driver to be used by default. See https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/
Pins used by the Amp2: GPIO 2, 3 (i2c pins 3 and 5), 18, 19, 20, 21 (pins 12, 35, 38, 40) GPIO4 will mute output when pulled low. 

Pins 11, 13,15 are used by the rotary encoder. GPIO 17 (DT), 27 (CLK), 22 (Switch).

Kivy installation on a Raspberry Pi (installed from source running on top of x11 and the pi DE): https://kivy.org/doc/stable/installation/installation-rpi.html#install-source-rpi
It would be more efficient to run the kivy application with no desktop environment. 