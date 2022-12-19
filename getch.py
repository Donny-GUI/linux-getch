import tty
import termios
import sys


def linux_getch():
    # get the last stdin character
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)
    # special case, character is space
    if ch == ' ':
        return 'space'
    # use ordinal value to determine if an escape sequence was used
    ordch = ord(ch)
    match ordch:
        case 13:
            return 'enter'
        case 9:
            return 'tab'
        case 127:
            return 'backspace'
        case other:
            return ch
