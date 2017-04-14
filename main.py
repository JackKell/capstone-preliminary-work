from scipy.signal import periodogram
from scipy.signal import chirp
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write

samples = 44100
time = 1000
t = np.linspace(0, time, samples)
w = chirp(t, f0=1, f1=25, t1=time, method='linear')
scaled = np.int16(w/np.max(np.abs(w)) * 32767)
write("test.wav", samples, scaled)

# plt.plot(t, w)
# plt.show()

# References
# How to use scipy chirp
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.chirp.html
# How to write wave files
# http://stackoverflow.com/questions/10357992/how-to-generate-audio-from-a-numpy-array