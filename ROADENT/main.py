from ROADENT.App.Voice_Commands import Voice_Commands
from ROADENT.App import *

if __name__ == "__main__":

    while True:
        Motor_1.clockwise()
        Motor_2.c_clockwise()
        Voice_Commands()