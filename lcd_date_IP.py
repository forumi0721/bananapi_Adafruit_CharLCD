#!/usr/bin/env python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd = "ip addr show eth0 | grep inet -m 1 | awk '{print $2}' | cut -d/ -f1"

lcd.begin(20, 1)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    lcd.clear()
    ipaddr = run_cmd(cmd)
    lcd.message(datetime.now().strftime('%Y-%m-%d  %p %I:%M\n'))
    lcd.message('IP %s\n' % (ipaddr))
    sleep(60)
