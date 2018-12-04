import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [5,5,5,5,4,4,1,1,1,1,1,1]

plt.figure(figsize=(6,2.0), dpi=80)

plt.vlines(x, 0, y, linestyle="solid", linewidth=3.0)
#plt.hlines(y, 0, x, linestyle="dashed")
plt.scatter(x, y, zorder=2, color="black")

plt.xlabel('CPU ID', fontsize=10)
plt.ylabel('Máx. tuplas na fila', fontsize=10)
plt.legend(['Caso 2'], fontsize='small', shadow=True, fancybox=True)

plt.yticks(np.arange(0, 30, step=10))

plt.text(1.5, 10, r'falha')
plt.vlines(0.7, 0, 8, linestyle="dashed", linewidth=0.8)
plt.vlines(3.3, 0, 8, linestyle="dashed", linewidth=0.8)
plt.hlines(8, 0.7, 3.3, linestyle='dashed', linewidth=0.8)

plt.xlim(0,None)
plt.ylim(0,20)

plt.savefig('queue_case2.eps')

