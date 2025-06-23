# IPA TTS
**IPA TTS** is a Python wrapper around [eSpeak NG](https://github.com/espeak-ng/espeak-ng) and 
the `py-espeak-ng` library. \
eSpeak NG is a powerful offline text-to-speech engine with support for many languages and its 
own phoneme system—but it lacks native support for the International Phonetic Alphabet (IPA). \
This library adds a lightweight layer that translates IPA symbols into eSpeak-compatible phonemes, 
allowing you to synthesize IPA-based input using eSpeak NG directly from Python.

## Example

```python
from ipatts import IPATTS

tts = IPATTS(volume=150, pitch=40, speed=150, voice='en')
tts.say("t͡ʃæt")  # says "chat"