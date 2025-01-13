from RPLCD.i2c import CharLCD
from gpiozero import Button
from signal import pause

lcd = CharLCD('PCF8574', 0x27)
btn = Button(4)
supported_apps = ["Fusion 360", "Blender", "Lego Studio"]
CURRENT_POS = 0


def cycle():
    global CURRENT_POS
    CURRENT_POS += 1
    if CURRENT_POS > len(supported_apps) - 1:
        CURRENT_POS = 0


btn.when_activated = cycle
lcd.write_string(supported_apps[CURRENT_POS])
pause()
