#!/usr/bin/env python3

import sleep_sound
import sound_go_boom_class
import argument
from time import sleep

if(__name__ == "__main__"):
    while True:
        argument.ParseArguments()
        sleep_sound.SetBoomingTime()
        sleep_sound.GoBoom()
        sleep(1)