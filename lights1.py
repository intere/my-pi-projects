#!/usr/bin/python
#
# This program assumes you have 3 LEDs wired up to Ground (GND) with a 100K Ohm
# resister between GND and the LED, and each LED is on a single port:
# 1 on 25, 1 on 24, 1 on 23.
#
# It also assumes you have RPIO installed. (https://github.com/metachris/RPIO) 
# This application must be run with Root Priviledges (either as root, or via sudo)
#

import RPIO
import time

RPIO.setup(25, RPIO.OUT)
RPIO.setup(24, RPIO.OUT)
RPIO.setup(23, RPIO.OUT)

for i in range(0, 257):
	RPIO.output(25, (i % 2 == 0))
	RPIO.output(24, (i % 3 == 0))
	RPIO.output(23, (i % 4 == 0))
	time.sleep(0.3)

RPIO.cleanup()

