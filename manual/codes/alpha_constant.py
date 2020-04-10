import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import style

#only beta is varied


a=[0.01]
b=[1.1, 2.1, 3.1, 4.1, 4.8]
plt.figure()
for i in range(0,5):
    system= signal.lti([1,2*b[i]+2],[ 1, 2*b[i], 0.01])
    w, mag, phase =signal.bode(system)
    plt.semilogx(w, mag)    
plt.legend()
plt.xlabel ("Frequency")
plt.ylabel ("Magnitude")
plt.show()
