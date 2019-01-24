import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1250,11250,1250)

plt.plot(x, [7999, 3999, 2666, 2020, 1599, 1342, 1142, 980],  color='black', linestyle=':')
plt.plot(x, [8109, 4054, 2700, 2027, 1621, 1351, 1157, 1013],  marker="^", color='b')
plt.plot(x, [8900, 4480, 2945, 2209, 1804, 1472, 1218.96, 1135],  marker="d", color='r')
plt.plot(x, [16527, 7404, 6040, 4131, 3354, 2222, 1781, 2004],  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3', 'Case 4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate (s)', fontsize=12)
plt.ylabel('Latency (s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 11250, step=1250), size=12)
plt.yticks(np.arange(0, 20000, step=2000), size=12)
#plt.margins(0)

plt.tight_layout()


plt.savefig('latency_cases.eps')
