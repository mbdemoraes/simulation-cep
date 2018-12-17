import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1250,11250,1250)

#DiscardsFree = [136253, 135038, 135030,135081, 131299, 135060, 131312, 130091]
#DiscardsFailure = [1124950, 1200026, 1046295, 1045063, 1275085, 1042595, 665040, 1350065, 810060]
#DiscardsCase3 = [10658698, 10962836, 6667757, 5591435, 10040372]

plt.plot(x, [1233, 2466, 3703, 6138, 6169, 7401, 8643, 9871],  marker="^", color='b')
plt.plot(x, [1123, 2232, 3395, 4526, 5543, 6793, 8210, 8810],  marker="d", color='r')
plt.plot(x, [605, 1350, 1655, 2420, 2981, 4500, 5614, 4990],  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate', fontsize=12)
plt.ylabel('Latency (s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 12500, step=1250), size=12)
plt.yticks(np.arange(0, 14000, step=2000), size=12)
plt.margins(0)

plt.tight_layout()


plt.savefig('throughput.eps')
