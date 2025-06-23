import os
import espeakng
import subprocess
import playsound

nasals = {
    "m̥": "hm",
    "m": "m",
    "ɱ": "F",
    "n̥": "hn",
    "n": "n",
    "ɳ̊": "n`",
    "ɳ": "n`",
    "ɲ̟̊": "hn`",
    "ɲ̟": "",
    "ɲ̊": "",
    "ɲ": "",
    "ŋ̊": "",
    "ŋ": "",
    "ɴ̥": "",
    "ɴ": "",
    "ŋ͡m": ""
}

stops = {
    "p": "",
    "b": "",
    "p̪": "",
    "b̪": "",
    "t̪": "",
    "d̪": "",
    "t": "",
    "d": "",
    "ʈ": "",
    "ɖ": "",
    "c": "",
    "ɟ": "",
    "k": "",
    "ɡ": "",
    "q": "",
    "ɢ": "",
    "ʡ": "",
    "ʔ": "",
    "k͡p": "",
    "ɡ͡b": ""
}

affricates = {
    "t͡s": "",
    "d͡z": "",
    "t͡ʃ": "",
    "d͡ʒ": "",
    "ʈ͡ʂ": "",
    "ɖ͡ʐ": "",
    "t͡ɕ": "",
    "d͡ʑ": "",
    "p͡ɸ": "",
    "b͡β": "",
    "p̪͡f": "",
    "b̪͡v": "",
    "t͡θ": "",
    "d͡ð": "",
    "c͡ç": "",
    "ɟ͡ʝ": "",
    "k͡x": "",
    "ɡ͡ɣ": "",
    "q͡χ": "",
    "ɢ͡ʁ": "",
    "ʡ͡ħ": "",
    "ʡ͡ʕ": "",
    "ʔ͡h": "",
    "t͡ɬ": "",
    "d͡ɮ": "",
    "ʈ͡ɭ̊˔": "",
    "c͡ʎ̥˔": "",
    "k͡ʟ̝̊": "",
    "ɡ͡ʟ̝": "",
    "p͡f": "",
    "b͡v": ""
}

fricatives = {
    "s": "",
    "z": "",
    "ʃ": "",
    "ʒ": "",
    "ʂ": "",
    "ʐ": "",
    "ɕ": "",
    "ʑ": "",
    "ɸ": "",
    "β": "",
    "f": "",
    "v": "",
    "θ": "",
    "ð": "",
    "ç": "",
    "ʝ": "",
    "x": "",
    "ɣ": "",
    "χ": "",
    "ʁ": "",
    "ħ": "",
    "ʕ": "",
    "h": "",
    "ɬ": "",
    "ɮ": "",
    "ɭ̊˔": "",
    "ʎ̥˔": "",
    "ʎ̝": "",
    "ʟ̝̊": "",
    "ʟ̝": "",
    "ɧ": ""
}

approximants = {
    "ʋ̥": "",
    "ʋ": "",
    "ɹ̥": "",
    "ɹ": "",
    "ɻ̊": "",
    "ɻ": "",
    "j̊": "",
    "j": "",
    "ɰ̊": "",
    "ɰ": "",
    "l̥": "",
    "l": "",
    "ɭ̊": "",
    "ɭ": "",
    "ʎ̥": "",
    "ʎ": "",
    "ʟ̥": "",
    "ʟ": "",
    "ʟ̠": "",
    "ɥ": "",
    "ʍ": "",
    "w": "",
    "ɫ": ""
}

taps_flaps = {
    "ⱱ̟": "",
    "ⱱ": "",
    "ɾ̥": "",
    "ɾ": "",
    "ɽ̊": "",
    "ɽ": "",
    "ɢ̆": "",
    "ʡ̮": "",
    "ɺ": "",
    "ɭ̆": "",
    "ʎ̮": "",
    "ʟ̆": "",
}

trills = {
    "ʙ": "",
    "r̥": "",
    "r": "",
    "ɽ͡r̥": "",
    "ɽ͡r": "",
    "ʀ̥": "",
    "ʀ": "",
    "ʜ": "",
    "ʢ": "",
}

special = {
    # Clicks
    "ʘ": "",
    "ǀ": "",
    "ǃ": "",
    "ǂ": "",
    "ǁ": "",

    # Implosives
    "ɓ": "",
    "ɗ": "",
    "ʄ": "",
    "ɠ": "",
    "ʛ": "",

    # Ejectives
    "pʼ": "",
    "tʼ": "",
    "ʈʼ": "",
    "cʼ": "",
    "kʼ": "",
    "qʼ": "",
    "ʡʼ": "",
    "fʼ": "",
    "θʼ": "",
    "sʼ": "",
    "ʃʼ": "",
    "ʂʼ": "",
    "xʼ": "",
    "χʼ": "",
    "ɬʼ": "",

    "͡": ""
}

vowels = {
    "i": "",
    "y": "",
    "ɨ": "",
    "ʉ": "",
    "ɯ": "",
    "u": "",
    "ɪ": "",
    "ʏ": "",
    "ʊ": "",
    "e": "",
    "ø": "",
    "ɘ": "",
    "ɵ": "",
    "ɤ": "",
    "o": "",
    "ə": "",
    "ɛ": "",
    "œ": "",
    "ɜ": "",
    "ɞ": "",
    "ʌ": "",
    "ɔ": "",
    "æ": "",
    "ɐ": "",
    "a": "",
    "ɶ": "",
    "ɑ": "",
    "ɒ": ""
}

ipa_to_espeak = {}
ipa_to_espeak.update(nasals)
ipa_to_espeak.update(stops)
ipa_to_espeak.update(affricates)
ipa_to_espeak.update(fricatives)
ipa_to_espeak.update(approximants)
ipa_to_espeak.update(taps_flaps)
ipa_to_espeak.update(trills)
ipa_to_espeak.update(special)
ipa_to_espeak.update(vowels)


def _convert_ipa(ipa_string):
    for ipa, replacement in ipa_to_espeak.items():
        og_string = ipa_string
        ipa_string = ipa_string.replace(ipa, replacement)
        if og_string != ipa_string:
            print(ipa, ": ", replacement)
    return ipa_string


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
        phonemes = _convert_ipa(ipa)
        txt = "[[" + phonemes + "]]"
        print(phonemes)

        args = [txt.encode('utf8')]

        self._espeak_exe(args)
