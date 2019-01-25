import matplotlib.pyplot as plt
import numpy as np


y = np.arange(1,11,1)


plt.subplot(211)
plt.plot(y, [201, 404, 608, 809, 1012, 1215, 1418, 1620, 1823, 2026],  marker="^", color='#000000')
plt.plot(y, [201, 404, 607, 809, 1013, 1216, 1418, 1621, 1824, 2027],  color='#e5914b')
plt.plot(y, [0,0,1,0,1,1,0,1,1,1],  linestyle=':', color='#000000')

plt.legend(['simulation', 'analytic model', 'simulation % error'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processing window ( x $\mathregular{10^6}$) for failure-free', fontsize=12)
plt.ylabel('Latency (s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1, 11, step=1), size=12)
plt.yticks(np.arange(0, 2400, step=400), size=12)
plt.margins(0)

plt.tight_layout()

plt.subplot(212)
plt.plot(y, [201, 405, 669, 871, 1074, 1277, 1479, 1682, 1946, 2149],  marker="^", color='#000000')
plt.plot(y, [224, 463, 703, 929, 1170, 1410, 1636, 1875, 2115, 2355],  color='#e5914b')
plt.plot(y, [23, 58, 34, 58, 96, 133, 157, 193, 169, 206],  linestyle=':', color='darkslateblue')

plt.legend(['simulation', 'analytic model', 'simulation % error'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processing window ( x $\mathregular{10^6}$) for failure-prone', fontsize=12)
plt.ylabel('Latency (s)', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1, 11, step=1), size=12)
plt.yticks(np.arange(0, 2400, step=400), size=12)
plt.margins(0)

plt.tight_layout()

plt.savefig('latency.eps')
