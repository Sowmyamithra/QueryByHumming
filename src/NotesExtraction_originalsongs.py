import numpy as np
import wave
import struct
from glob import glob
import NotesExtraction_main as ne

data_dir = '.\Hummed_Files';
audio_files = glob(data_dir + '/*.wav');
for i in range(0 , len(audio_files)):
 sound_file = wave.open(audio_files[0])
 ne.play(sound_file);