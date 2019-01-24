import matplotlib.pyplot as plt
import numpy as np
from math import log10


x = np.arange(1250, 11250, 1250)
yCase1 = [136253, 135038, 135030, 135081, 131299, 135060, 131312, 130091]
yCase2 = [1124950, 1200026, 1046295, 1045063, 1275086, 1042595, 665040, 1350065]
yCase3 = [10658698, 8510122, 12652660, 10655213, 10962836, 6667757, 5591435, 10040372]

plt.plot(x, [0,0,0,0,0,0,0,0],  color='black', linestyle=':')
plt.plot(x, yCase1,  marker="^", color='b')
plt.plot(x, yCase2,  marker="d", color='r')
plt.plot(x, yCase3,  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3', 'Case 4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate', fontsize=12)
plt.ylabel('Discards ($\mathregular{10^7}$)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 12500, step=1250), size=12)
plt.yticks(np.arange(0, 16000000, step=2000000), size=12)
#plt.margins(0)

plt.tight_layout()


plt.savefig('discards_cases.eps')
