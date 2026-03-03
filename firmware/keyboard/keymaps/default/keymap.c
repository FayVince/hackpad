#include QMK_KEYBOARD_H

enum layers {
    _BASE
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_BASE] = LAYOUT(
        KC_RGHT,  // GP1
        KC_DOWN,  // GP2
        KC_LEFT,  // GP3
        KC_UP,    // GP4
        KC_DEL,   // GP6
        KC_MUTE   // GP9 (encoder switch)
    )
};

bool encoder_update_user(uint8_t index, bool clockwise) {
    if (clockwise) {
        tap_code(KC_VOLU);
    } else {
        tap_code(KC_VOLD);
    }
    return false;
}