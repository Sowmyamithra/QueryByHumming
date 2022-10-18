#reading input from user and saving onto local folder

import pyaudio;
import wave;

filename = input("Enter file name : ");             # the file name output you want to record into
filename = filename + ".wav";
chunk = 1024;                                       # set the chunk size of 1024 samples
FORMAT = pyaudio.paInt16;                           # sample format
channels = 1;                                       # mono, change to 2 if you want stereo
sample_rate = 44100;                                # 44100 samples per second
record_seconds = 5;
p = pyaudio.PyAudio();                              # initialize PyAudio object
stream = p.open(format=FORMAT,
                channels=channels,
                rate=sample_rate,
                input=True,
                output=True,
                frames_per_buffer=chunk);           # open stream object as input & output
frames = [];
print("Recording...");
for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk);
    # if you want to hear your voice while recording
    # stream.write(data)
    frames.append(data);
print("Finished recording.");
stream.stop_stream();                               # stop and close stream
stream.close();
p.terminate();                                      # terminate pyaudio object
wf = wave.open(filename, "wb");                     # save audio file abd open the file in 'write bytes' mode
wf.setnchannels(channels);                          # set the channels
wf.setsampwidth(p.get_sample_size(FORMAT));         # set the sample format
wf.setframerate(sample_rate);                       # set the sample rate
wf.writeframes(b"".join(frames));                   # write the frames as bytes
wf.close();                                         # close the file

# move the file to Hummed_Files folder

import shutil
import os;
files = [filename];
for f in files:
    shutil.move(f, 'InputRecordings');

