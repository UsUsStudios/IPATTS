import os

import espeakng
import subprocess
import playsound


class IPATTS:
    def __init__(self,
                 volume: int = 100,
                 pitch: int = 50,  # 0-99
                 speed: int = 175,  # approximate words per minute
                 voice: str = 'en') -> None:
        self.volume = volume,
        self.pitch = pitch,
        self.speed = speed,
        self.voice = voice

    def _espeak_exe(self, args):
        cmd = [
            "C:/Program Files/eSpeak NG/espeak-ng.exe",
            '-a', str(self.volume[0]),
            '-p', str(self.pitch[0]),
            '-s', str(self.speed[0]),
            '-v', self.voice,
            '-b', '1',  # UTF8 text encoding
            '-w', "output.wav"
        ]
        cmd.extend(args)
        subprocess.run(cmd)
        playsound.playsound("output.wav")

    def say(self, ipa: str):
        txt = "[[" + ipa + "]]"
        print(ipa)

        args = [txt.encode('utf8')]

        self._espeak_exe(args)
