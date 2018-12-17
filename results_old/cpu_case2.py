import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [12.55,7.01,6.20,28.41,1.61,1.345,31.36,0.03,0.004,31.36,0.12,0]

plt.figure(figsize=(6,2.0), dpi=80)

plt.vlines(x, 0, y, linestyle="solid", linewidth=3.0)
#plt.hlines(y, 0, x, linestyle="dashed")
plt.scatter(x, y, zorder=2, color="black")

plt.xlabel('CPU ID', fontsize=10)
plt.ylabel('Uso de CPU (%)', fontsize=10)
plt.legend(['Caso 2'], fontsize='small', shadow=True, fancybox=True)

plt.yticks(np.arange(0, 60, step=20))

plt.text(1.5, 18, r'falha')
plt.vlines(0.7, 0, 16, linestyle="dashed", linewidth=0.8)
plt.vlines(3.3, 0, 16, linestyle="dashed", linewidth=0.8)
plt.hlines(16, 0.7, 3.3, linestyle='dashed', linewidth=0.8)

plt.xlim(0,None)
plt.ylim(0,40)

plt.savefig('cpu_case2.eps')

