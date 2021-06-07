from ROADENT.App.Voice_Commands import voice_commands
from ROADENT.App import *

if __name__ == "__main__":

    while True:
        Motor_1.clockwise()
        Motor_2.c_clockwise()
        voice_commands()
