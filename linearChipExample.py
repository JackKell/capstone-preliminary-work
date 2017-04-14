import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt

startTime = 0
endTime = 10
samples = int(40e3)
times = np.linspace(startTime, endTime, samples)
linearChirp = chirp(times, f0=5, f1=10, t1=10, method='linear')
plt.plot(times, linearChirp)
plt.show()
