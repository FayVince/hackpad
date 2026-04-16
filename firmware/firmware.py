import board
import microcontroller
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys  # <-- HELYES IMPORT (extensions, nem modules)

keyboard = KMKKeyboard()

# Hozzáadjuk a MediaKeys kiterjesztést a billentyűzethez
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = [
    board.A2,
    board.A1,
    board.A0,
    board.A3,
    board.SCL,
    board.SCK,
]

keyboard.row_pins = [board.TX]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LEFT, KC.DOWN, KC.RIGHT, KC.UP, KC.ESC, KC.MUTE]
]

encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.MISO, board.MOSI),
)

# KC.VOLD = Volume Down (Hangerő le), KC.VOLU = Volume Up (Hangerő fel)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]

keyboard.modules.append(encoder_handler)

try:
    keyboard.go()

except Exception as e:
    print("HIBA:", e)
    time.sleep(3)
    microcontroller.reset()

