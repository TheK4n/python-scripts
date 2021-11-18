#!/usr/bin/env python3
import math
import wave
import struct

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in
# memory.


class Wave:

    def __init__(self, filename: str, sample_rate=44100.0):
        self.filename = filename
        self.sample_rate = sample_rate
        self.audio = []

    def append_silence(self, duration_milliseconds=500):
        num_samples = duration_milliseconds * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(0.0)

        return

    def append_sinewave(self,
                        freq=440.0,
                        duration_milliseconds=250,
                        volume=1.0):
        num_samples = duration_milliseconds * (self.sample_rate / 1000.0)

        for x in range(int(num_samples)):
            self.audio.append(volume * math.sin(2 * math.pi * freq * (x / self.sample_rate)))

        return

    def save_wav(self):
        # Open up a wav file
        wav_file = wave.open(self.filename, "w")

        # wav params
        nchannels = 1

        sampwidth = 2

        # 44100 is the industry standard sample rate - CD quality.  If you need to
        # save on file size you can adjust it downwards. The stanard for low quality
        # is 8000 or 8kHz.
        nframes = len(self.audio)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sampwidth, self.sample_rate, nframes, comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the
        # sample size.  So we multiply the floating point data we have by 32767, the
        # maximum value for a short integer.  NOTE: It is theortically possible to
        # use the floating point -1.0 to 1.0 data directly in a WAV file but not
        # obvious how to do that using the wave module in python.
        for sample in self.audio:
            wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))

        wav_file.close()


if __name__ == '__main__':
    w = Wave("output.wav")

    w.append_sinewave(volume=0.25, duration_milliseconds=150)
    w.append_sinewave(volume=0.25, duration_milliseconds=150)
    w.append_silence()
    w.append_sinewave(volume=0.5, duration_milliseconds=500)
    w.append_silence()
    w.append_sinewave(volume=0.25, duration_milliseconds=150)
    w.append_silence()
    w.append_sinewave(volume=0.5, duration_milliseconds=500)
    w.append_silence()
    w.append_sinewave(volume=0.25, duration_milliseconds=150)
    w.append_silence()
    w.append_sinewave(volume=0.5, duration_milliseconds=500)
    w.append_silence()
    w.save_wav()
