#!/usr/bin/python
# -*- coding: utf-8 -*-

import scipy as sp
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.fftpack
import cmath

fn='blues.00000.wav'
sample_rate, x = sp.io.wavfile.read(fn)
x = x / (max(abs(X))+0.0)

x = sp.sin(2*sp.pi*sp.linspace(0,20,1000))
start = 0
N = 256

X = sp.fft(x[start:start+N])

freqList = sp.fftpack.fftfreq(N, d = 1.0/ sample_rate)

amplitudeSpectrum = abs(X)
phaseSpectrum = sp.angle(X)

plt.plot(range(start,start+N),x[start:start+N])
plt.show()

plt.plot(freqList,amplitudeSpectrum,'o-',)
plt.show()

plt.plot(freqList,phaseSpectrum,"o-")
plt.show()
