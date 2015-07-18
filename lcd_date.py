#!/usr/bin/env python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

lcd.begin(20, 1)

while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%Y-%m-%d  %p %I:%M\n'))
    sleep(60)
