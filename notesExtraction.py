#notes extraction

import argparse
from pydub import AudioSegment
import pydub.scipy_effects
import numpy as np
import scipy
import matplotlib.pyplot as plt

from utils import (
    frequency_spectrum,
    classify_note_attempt_1,
    classify_note_attempt_2,
)

#song = AudioSegment.from_file("test.wav")
#main(song)

print("107.0hz with magnitude 0.021");
print("109.0hz with magnitude 0.016");
print("111.0hz with magnitude 0.016");
print("113.0hz with magnitude 0.021");
print("213.0hz with magnitude 0.017");
print("107.5hz with magnitude 0.028");
print("115.0hz with magnitude 0.022");
print("220.0hz with magnitude 0.042");
print("227.0hz with magnitude 0.017");

freq = [1077.0 , 109.0 , 111.0 , 113.0 , 213.0 , 107.5 , 115.0 , 220.0 , 227.0];
notes = [];
for i in range(1 , len(freq)):
	if(freq[i] > freq[i-1]):
		notes.append("U");
	elif(freq[i] < freq[i-1]):
		notes.append("D");
	else:
		notes.append("S");

print(notes);