#!/usr/bin/env python

# Copyright Boris Tekaty 2018
# Distributed under Apache 2 license

import time
import pigpio

pi = pigpio.pi()
freq=5000

if not pi.connected:
   exit()
# For some reason the signal from the PCB module is inverted
# therefore we need to invert PWM signal like inv_pwm=100-pwm

min_pwm = 000000
max_pwm = 1100000
step_pwm = 100000

for pwm in range(min_pwm, max_pwm, step_pwm):
   # invert pwm here
   inv_pwm = 1000000 - pwm
   pi.hardware_PWM(18, freq, inv_pwm) # 500000 for square wave.
   print("\n12 set {} got {} inv_pwm={}%".format(
     freq, pi.get_PWM_frequency(18),inv_pwm/10000))
   time.sleep(5)

pi.hardware_PWM(18, 0, 0)

pi.stop()
