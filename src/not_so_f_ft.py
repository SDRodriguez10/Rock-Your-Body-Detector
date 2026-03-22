#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import librosa

#audio_data, sampling_rate = librosa.load('../data/RUB.mp3')

tot_time = (len(audio_data)/sampling_rate)/60
print("\nThe MP3 I used was 4 Mins 57 Secs so if you try this with your own MP3 and it's not exactly that long then I can't gurantee anything sorry :,(")
print(f"\nNum samps: {len(audio_data)}, \nSampling Rate: {sampling_rate},\nSong Duration: {int(tot_time)} Minutes {int((tot_time - int(tot_time))*60)} Seconds\n")

# power of 2 because Joseph Fourier was exceptionally Autistic and obessed with powers of 2
fft_size = 1024


# First I want to do the whole O(N^2) fourier transform
# you know the one
# X[k] = sum_(n=0)_(n=N){x[n]*complex_sine} 
# yes that one

