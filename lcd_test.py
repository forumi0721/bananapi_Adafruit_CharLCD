#!/usr/bin/env python

from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD()

lcd.begin(20, 1)

lcd.clear()

lcd.message("Line 1        Line 1\nLine 2        Line 2\nLine 3        Line 3\nLine 4        Line 4")

