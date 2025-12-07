import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.NO,
     KC.SPC,
     KC.Z,
     KC.NO,
     KC.NO,
     KC.C,
     KC.SPC,
     KC.NO,
     KC.NO,
     KC.LSHIFT,
     KC.LCTRL,
     KC.NO,
     KC.NO,
     KC.V,
     KC.B,
     KC.NO,
     KC.CAPS,
     KC.LALT,
     KC.A,
     KC.S,
     KC.NO,
     KC.D,
     KC.F,
     KC.G,
     KC.R,
     KC.TAB,
     KC.Q,
     KC.W,
     KC.NO,
     KC.E,
     KC.R,
     KC.NO,
     KC.EQL,
     KC.N1,
     KC.N2,
     KC.N3, 
     KC.N4,
     KC.N5,
     KC.N6,
     KC.T,
     KC.TILDE,
     KC.N7,
     KC.N8,
     KC.NO,
     KC.N9,
     KC.N0,
     KC.F1,
     KC.PGDN,
     KC.INS,
     KC.ESC,
     KC.NO,
     KC.NO,
     KC.NO,
     KC.NO,
     KC.PSCR,
     KC.PGUP,
     KC.AUDIO_VOL_DOWN,
     KC.AUDIO_VOL_UP,
     KC.AUDIO_MUTE,
     KC.MEDIA_PREV_TRACK,
     KC.MEDIA_PLAY_PAUSE,
     KC.MEDIA_STOP,
     KC.MEDIA_NEXT_TRACK]
]

if __name__ == '__main__':
    keyboard.go()
