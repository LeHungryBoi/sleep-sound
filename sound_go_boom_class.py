import os
import sys


if (sys.platform == 'win32'):
    from winsound import PlaySound
#if (sys.platform == 'linux'):
#    from playsound import PlaySound

class soundgoboom:
    def __init__(self, name):
        self.name = name

    current_os = sys.platform

    def SoundGoBoom (audio_file):
        if(sys.platform == 'linux'):
            print(audio_file)
            os.system('aplay ' + audio_file)
            
        elif(sys.platform == 'win32'):
            PlaySound(audio_file, False)
