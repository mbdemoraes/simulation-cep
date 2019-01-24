import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1250,11250,1250)

plt.plot(x, [0,0,0,0,0,0,0,0],  color='black', linestyle=':')
plt.plot(x, [0,0,0,0,0,0,0,0],  marker="^", color='b')
plt.plot(x, [614705, 612290, 478563, 584992, 982500, 401754, 373926, 508584],  marker="d", color='r')
plt.plot(x, [1181285, 1122515, 956251, 1799996, 843745, 1237573, 181187, 2250111],  marker="P", color='g')

plt.legend(['Case 1', 'Case 2', 'Case 3', 'Case 4'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Arrival rate', fontsize=12)
plt.ylabel('Unprocessed tuples', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1250, 12500, step=1250), size=12)
plt.yticks(np.arange(0, 2400000, step=400000), size=12)
#plt.margins(0)

plt.tight_layout()


plt.savefig('unprocessed.eps')
