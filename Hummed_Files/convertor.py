#getting file from server adn converting to .wav format

import os
import shutil
from os import path
from pydub import AudioSegment

src = 'C:/Program Files/Apache Software Foundation/Tomcat 10.0_Tomcat10.0.0/test.wav'
dst = 'C:/Users/Dell/OneDrive/Desktop/project/Hummed_Files'
dest = shutil.move(src, dst)


#src = "test1.mp3"
#dst = "test.wav"
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")
