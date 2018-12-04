import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
Y = [22.30,17.10,15.67,55.68,4.729,2.27,54.44,0.66,0.01,62.16,0.50,0.01]



plt.figure(figsize=(6,2.0), dpi=80)

plt.vlines(x, 0, y, linestyle="solid", linewidth=3.0)
#plt.hlines(y, 0, x, linestyle="dashed")
plt.scatter(x, y, zorder=2, color="black")

plt.xlabel('CPU ID', fontsize=10)
plt.ylabel('Uso de CPU (%)', fontsize=10)
plt.legend(['Caso 4'], fontsize='small', shadow=True, fancybox=True)

plt.yticks(np.arange(0, 100, step=20))
plt.text(1.5, 40, r'falha')
plt.vlines(0.7, 0, 38, linestyle="dashed", linewidth=0.8)
plt.vlines(3.3, 0, 38, linestyle="dashed", linewidth=0.8)
plt.hlines(38, 0.7, 3.3, linestyle='dashed', linewidth=0.8)
plt.text(7.5, 62, r'falha')
plt.vlines(6.7, 0, 60, linestyle="dashed", linewidth=0.8)
plt.vlines(9.3, 0, 60, linestyle="dashed", linewidth=0.8)
plt.hlines(60, 6.7, 9.3, linestyle='dashed', linewidth=0.8)


plt.xlim(0,None)
plt.ylim(0,80)

plt.savefig('cpu_case4.eps')

