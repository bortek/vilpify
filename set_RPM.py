#!/usr/bin/env python

# Copyright Boris Tekaty 2018
# Distributed under Apache 2 license

import time
import pigpio

freq=5000
GPIO=18
# pwm example , if you want 10% then set pwm=100000, 90%=900000
pwm=300000

# TODO
# Limit max PWM to 90% to save the motor

pi = pigpio.pi()

if not pi.connected:
   exit()
# For some reason the signal from the PCB module is inverted
# therefore we need to invert PWM signal like inv_pwm=100-pwm

# enable this if you want to invert pwm
#set_pwm = 1000000 - pwm
set_pwm = pwm 
pi.hardware_PWM(GPIO, freq, set_pwm) # 500000 for square wave.
#print("\nSetting PWM to {e} got {} Setting PWM to {}%".format(freq, pi.get_PWM_frequency(GPIO),set_pwm/10000))
time.sleep(3)

# Set rpm to 0 by sending PWM 0
#pi.hardware_PWM(GPIO, 0, 0)

pi.stop()
