#!/usr/bin/env python

# Copyright Boris Tekaty 2018
# Distributed under Apache 2 license

import time
import pigpio
import argparse

freq=5000
GPIO=18
min_percent=0
max_percent=80

# pwm example in case of hard coding them. If you want 10% then set pwm=100000, 90%=900000
#pwm=200000
#pwm=400000
#pwm=350000

# parsing arguments
# Limit max PWM to 80% to spare the motor
def range_type(astr, min=min_percent, max=max_percent):
    value = int(astr)
    if min<= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError('value not in range %s-%s'%(min,max))

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--percent', dest='speed_percent', type=range_type,
                    help='Set fan speed to INTEGER percent. Values in range %s-%s are accepted.'%(min_percent,max_percent), metavar="[%s-%s]"%(min_percent,max_percent))
args = parser.parse_args()

# Setting PWM
pi = pigpio.pi()

if not pi.connected:
   exit()

# If you want to hard code pwm (taken from beginnig
# of file) then enable this and disable setting it from parsed arguments
#set_pwm = pwm 
set_pwm = args.speed_percent * 10000

pi.hardware_PWM(GPIO, freq, set_pwm) # 500000 for square wave.
#print("\nSetting PWM to {e} got {} Setting PWM to {}%".format(freq, pi.get_PWM_frequency(GPIO),set_pwm/10000))
time.sleep(3)

# Set rpm to 0 by sending PWM 0
#pi.hardware_PWM(GPIO, 0, 0)

pi.stop()
