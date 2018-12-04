import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [11,10,10,11,10,10,2,1,1,2,1,1]


plt.figure(figsize=(6,2.0), dpi=80)


plt.vlines(x, 0, y, linestyle="solid", linewidth=3.0)
#plt.hlines(y, 0, x, linestyle="dashed")
plt.scatter(x, y, zorder=2, color="black")

plt.xlabel('CPU ID', fontsize=10)
plt.ylabel('Máx. tuplas na fila', fontsize=10)
plt.legend(['Caso 4'], fontsize='small', shadow=True, fancybox=True)

plt.yticks(np.arange(0, 30, step=10))

plt.text(1.5, 16, r'falha')
plt.vlines(0.7, 0, 14, linestyle="dashed", linewidth=0.8)
plt.vlines(3.3, 0, 14, linestyle="dashed", linewidth=0.8)
plt.hlines(14, 0.7, 3.3, linestyle='dashed', linewidth=0.8)
plt.text(7.5, 14, r'falha')
plt.vlines(6.7, 0, 12, linestyle="dashed", linewidth=0.8)
plt.vlines(9.3, 0, 12, linestyle="dashed", linewidth=0.8)
plt.hlines(12, 6.7, 9.3, linestyle='dashed', linewidth=0.8)


plt.xlim(0,None)
plt.ylim(0,20)

plt.savefig('queue_case4.eps')

