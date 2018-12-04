import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [12.55,7.01,6.20,28.35,1.61,1.34,31.64,0.03,0,31.369,0.012,0]

plt.figure(figsize=(6.0,2.0), dpi=80)

plt.vlines(x, 0, y, linestyle="solid", linewidth=3.0)
#plt.hlines(y, 0, x, linestyle="dashed")
plt.scatter(x, y, zorder=2, color="black")

plt.xlabel('CPU ID', fontsize=10)
plt.ylabel('Uso de CPU (%)', fontsize=10)
plt.legend(['Caso 1'], fontsize='small', shadow=True, fancybox=True)

plt.yticks(np.arange(0, 50, step=20))

plt.xlim(0,None)
plt.ylim(0,None)

plt.savefig('cpu_case1.eps')

