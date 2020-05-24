# License
'''
Code by Deep
May 23,2020
Released under GNU GPL
'''

import numpy as np  
import matplotlib.pyplot as plt
import subprocess
import shlex

Data1 = np.loadtxt('ee18btech11011.dat')

plt.figure(figsize=(8.0,12.0))
plt.subplot(2,1,1)
plt.plot(Data1[:,0],Data1[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Closed-Loop System Response")
plt.title('Spice Simulation')
plt.show()

#If using termux
plt.savefig('../../figs/ee18btech11011/ee18btech11011_spice_result.pdf')
plt.savefig('../../figs/ee18btech11011/ee18btech11011_spice_result.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11011/ee18btech11011_spice_result.pdf"))
plt.show()
