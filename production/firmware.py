from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import RotaryEncoder

keyboard = KMKKeyboard()

# ----------------------
# GPIO kiosztás
# ----------------------
# gombok: GP1-jobb, GP2-le, GP3-bal, GP4-fel, GP6-del, GP9-mute
keyboard.col_pins = [board.GP1, board.GP2, board.GP3, board.GP4, board.GP6, board.GP9]
keyboard.row_pins = [board.GP0]  # 1 soros macropad
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----------------------
# Keymap
# ----------------------
keyboard.keymap = [
    [KC_RGHT, KC_DOWN, KC_LEFT, KC_UP, KC_DEL, KC_MUTE]
]

# ----------------------
# Rotary encoder
# ----------------------
encoder = RotaryEncoder(pin_num_a=board.GP11, pin_num_b=board.GP10)

@encoder.on_rotate
def vol(rot):
    if rot > 0:
        keyboard.tap_key(KC.VOLU)
    else:
        keyboard.tap_key(KC.VOLD)

@encoder.on_press
def mute():
    keyboard.tap_key(KC.MUTE)  # GP9 már fizikai gomb, de lehet encoder switch is

keyboard.modules.append(encoder)

if __name__ == '__main__':
    keyboard.go()