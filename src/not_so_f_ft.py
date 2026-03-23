#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import librosa

audio_data, sampling_rate = librosa.load("../data/RUB.mp3")
print(type(audio_data))
audio_data =  audio_data[0:1024*108] # just do first 108 windows
sampling_rate = 22050
print(audio_data[0:5])
tot_time = (len(audio_data)/sampling_rate)/60
print("\nThe MP3 I used was 4 Mins 57 Secs so if you try this with your own MP3 and it's not exactly that long then I can't gurantee anything sorry :,(")
print(f"\nNum samps: {len(audio_data)}, \nSampling Rate: {sampling_rate},\nSong Duration: {int(tot_time)} Minutes {int((tot_time - int(tot_time))*60)} Seconds\n")

# power of 2 because Joseph Fourier was exceptionally Autistic and obessed with powers of 2
fft_size = 1024
print(len(audio_data)/fft_size)
def complex_sine(k, lil_n, big_n):
    letter_five = 2.71828182845904523536
    pie         = 3.14159265358979323846
    complex_i   = 1j
    the_number_two = int(letter_five)
    complex_val = letter_five ** (-1 * complex_i * pie * the_number_two * k * lil_n / big_n)
    return complex_val

# First I want to do the whole O(N^2) fourier transform
# you know the one
# X[k] = sum_(n=0)_(n=N){x[n]*complex_sine} 
# yes that one
samps = []
n = np.arange(fft_size) # range doesnt work bc it's already numpy'd :,(
for idx in range(0, len(audio_data), fft_size):
    window = audio_data[idx:idx+fft_size]
    x = [0 + 0j]*fft_size
    for k in range(fft_size):
        x[k] = np.sum(window * complex_sine(k, n, fft_size))
    samps.append(x)

print(samps[0][:4]) 
