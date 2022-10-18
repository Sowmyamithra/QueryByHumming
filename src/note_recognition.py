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


def main(song, note_file=None, note_starts_file=None, plot_starts=False, plot_fft_indices=[]):
	starts = predict_note_starts(song, plot_starts)
	predicted_notes = predict_notes(song, starts, plot_fft_indices)
	#print(predicted_notes)

def predict_note_starts(song, plot):
	SEGMENT_MS = 50
	VOLUME_THRESHOLD = -35
	EDGE_THRESHOLD = 5
	MIN_MS_BETWEEN = 100
	song = song.high_pass_filter(80, order=4)
	volume = [segment.dBFS for segment in song[::SEGMENT_MS]]
	predicted_starts = []
	for i in range(1, len(volume)):
		if(volume[i] > VOLUME_THRESHOLD and volume[i] - volume[i - 1] > EDGE_THRESHOLD):
			ms = i * SEGMENT_MS
			predicted_starts.append(ms)
	return predicted_starts

def predict_notes(song, starts, plot_fft_indices):
	predicted_notes = []
	for i, start in enumerate(starts):
		sample_from = start + 50
		sample_to = start + 550
		if i < len(starts) - 1:
			sample_to = min(starts[i + 1], sample_to)
		segment = song[sample_from:sample_to]
		freqs, freq_magnitudes = frequency_spectrum(segment)
		#predicted = classify_note_attempt_2(freqs, freq_magnitudes)
		#predicted_notes.append(predicted or "U")
		#print("Predicted start: {}".format(start))
		length = sample_to - sample_from
		#print("Sampled from {} to {} ({} ms)".format(sample_from, sample_to, length))
		#print("Frequency sample period: {}hz".format(freqs[1]))
		peak_indicies, props = scipy.signal.find_peaks(freq_magnitudes, height=0.015)
		#print("Peaks of more than 1.5 percent of total frequency contribution:")
		for j, peak in enumerate(peak_indicies):
			freq = freqs[peak]
			magnitude = props["peak_heights"][j]
			print("{:.1f}hz with magnitude {:.3f}".format(freq, magnitude))
	notes1 = []
	for i in range(1 , len(freqs)):
		if(freqs[i] > freqs[i-1]):
			notes1.append("U");
		elif(freqs[i] < freqs[i-1]):
			notes1.append("D");
		else:	
			notes1.append("S");
	print(notes1);
	return predicted_notes

song = AudioSegment.from_file("test.wav")
main(song)
