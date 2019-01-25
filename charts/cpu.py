import matplotlib.pyplot as plt
import numpy as np


t = np.arange(1250, 10300, 1250)
x = [0.10,0.20,0.30,0.10,0.10,0.20,0.30,0.40]


plt.plot(t, x, marker="o", color='dodgerblue', linewidth=1.0,  ms=3.0)




#plt.legend(['CPU 1', 'CPU 2', 'CPU 3', 'CPU 4', 'CPU 5', 'CPU 6', 'CPU 7', 'CPU 8', 'CPU 9', 'CPU 10', 'CPU 11', 'CPU 12', ], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('arrival rate (s)', fontsize=10)
plt.ylabel('CPU load (%)', fontsize=10)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 10250, step=1250))
plt.yticks(np.arange(0, 1.20, step=0.20))
#plt.margins(0)

plt.tight_layout()

plt.savefig('cpu.eps')
