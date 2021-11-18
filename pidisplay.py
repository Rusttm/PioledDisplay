from digitalio import DigitalInOut
import time
import board
import digitalio
import pwmio
import adafruit_character_lcd.character_lcd as characterlcd

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True
