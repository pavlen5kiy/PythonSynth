import math
import itertools

from oscillator import *
from wave_to_file import *
from wave_adder import *


gen = WaveAdder(
    SineOscillator(freq=440),
    TriangleOscillator(freq=220, amp=0.8),
    SawtoothOscillator(freq=110, amp=0.6),
    SquareOscillator(freq=55, amp=0.4),
)
iter(gen)
wav = [next(gen) for _ in range(44100 * 4)] # 4 Seconds
wave_to_file(wav, fname="prelude_one.wav")
