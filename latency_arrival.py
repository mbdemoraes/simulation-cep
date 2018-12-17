import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1250,11250,1250)

#DiscardsFree = [136253, 135038, 135030,135081, 131299, 135060, 131312, 130091]
#DiscardsFailure = [1124950, 1200026, 1046295, 1045063, 1275085, 1042595, 665040, 1350065, 810060]
#DiscardsCase3 = [10658698, 10962836, 6667757, 5591435, 10040372, 10655213, 12652660, 8510122]

plt.plot(x, [8109, 4054, 2700, 1629, 1621, 1351, 1157, 1013],  marker="^", color='b')
plt.plot(x, [8900, 4480, 2945, 2209, 1804, 1472, 1218.96, 1135],  marker="d", color='r')
plt.plot(x, [16527, 7404, 6040, 4131, 3354, 2222, 1781, 2004],  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate', fontsize=12)
plt.ylabel('Latency (s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 11250, step=1250), size=12)
plt.yticks(np.arange(0, 24000, step=2000), size=12)
plt.margins(0)

plt.tight_layout()


plt.savefig('latency_cases.eps')
