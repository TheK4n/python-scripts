from src.sound import Wave
from morse_text import encode
from src.alphabet import *


def text_to_wav(text: str, speed=1.0, filename="morse.wav"):

    w = Wave(filename)
    dur = 150*speed
    for i in text.strip().split(" "):
        for e in i:
            if e == "-":
                w.append_sinewave(duration_milliseconds=dur*3, volume=0.5)  # beep duration of dash
            elif e == '.':
                w.append_sinewave(duration_milliseconds=dur, volume=0.5)  # beep duration of dot
            w.append_silence(duration_milliseconds=dur)  # pause duration between elements
        if i == '':
            w.append_silence(duration_milliseconds=dur*7/2)  # pause duration between words
        else:
            w.append_silence(duration_milliseconds=dur*3)  # pause duration between letters
    w.save_wav()


if __name__ == '__main__':
    text_to_wav(encode("сос сос сос", alphabet=rus), speed=0.5)
