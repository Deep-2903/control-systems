import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


#coefficents of open loop transfer function
num = [20,60]
den = [1,5,4,0]

#Transfer function GH = num/den
G = control.tf(num,den) 

#plotting nyquist plot
control.nyquist(G)


#if using termux
plt.savefig('./figs/ee18btech11011.pdf')
plt.savefig('./figs/ee18btech11011.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11011.pdf"))
#else
#plt.show()
