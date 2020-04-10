import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import style

#only alpha is varied


a=[0.01, 0.1, 1.1, 10, 20]
b=[0.01]
plt.figure()
for i in range(0,5):
    system= signal.lti([1,2*0.01+2],[ 1, 2*0.01, a[i]])
    w, mag, phase =signal.bode(system)
    plt.semilogx(w, mag)    
plt.legend()
plt.xlabel ("Frequency")
plt.ylabel ("Magnitude")
plt.show()
