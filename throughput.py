import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1250,11250,1250)

[7999, 3999, 2666, 2020, 1599, 1342, 1142, 980]

plt.plot(x, [1250, 2500, 3750, 4950, 6253, 7451, 8756, 10204],  color='black', linestyle=':')
plt.plot(x, [1233, 2466, 3703, 4933, 6169, 7401, 8643, 9871],  marker="^", color='b')
plt.plot(x, [1123, 2232, 3395, 4526, 5543, 6793, 8210, 8810],  marker="d", color='r')
plt.plot(x, [605, 1350, 1655, 2420, 2981, 4500, 5614, 4990],  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3', 'Case 4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate (s)', fontsize=12)
plt.ylabel('Throughput (tuples/s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 12500, step=1250), size=12)
plt.yticks(np.arange(0, 14000, step=2000), size=12)
plt.margins(0)

plt.tight_layout()


plt.savefig('throughput.eps')
