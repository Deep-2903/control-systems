#the transfer function = 20*300*0.0033/(0.001s^2+0.11s+1)

from scipy import signal
import matplotlib.pyplot as plt

system = signal.lti([20*300*0.0033], [0.001, 0.11, 1])

w, mag, phase = signal.bode(system)

plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, mag)    # Bode magnitude plot
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, phase)  # Bode phase plot
plt.ylabel("[degrees]")
plt.xlabel("[rad/s]")
plt.show()
