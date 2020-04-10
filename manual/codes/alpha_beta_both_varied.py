import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import style

# alpha(a) and beta(b) both are varied 



a=[0.01, 0.1, 1.1, 1, 5]
b=[0.01, 1.1, 0.1, 2, 2.1]
plt.figure()
for i in range(0,5):
    system= signal.lti([1,2*b[i]+2],[ 1, 2*b[i], a[i]])
    w, mag, phase =signal.bode(system)
    plt.semilogx(w, mag)    
plt.legend()
plt.xlabel ("Frequency")
plt.ylabel ("Magnitude")
plt.show()
