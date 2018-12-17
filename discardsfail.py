import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11,1)

#free
plt.plot(x, [9998, 25015, 40024, 50018, 65027, 80048, 95049, 105059, 120072, 135081], marker="x", linestyle="none", color='#000000')
plt.plot(x, [10000, 25000, 40000, 50000, 65000, 80000, 90000, 105000, 120000, 135000], linestyle=":", color='#e5914b')
#failure
plt.plot(x, [10000, 25007, 345039, 355041, 370046, 690030, 700032, 715000, 730042, 1045063], marker="s", linestyle="none", color='#000000')
plt.plot(x, [10000, 25000, 340000, 350000, 365000, 680000, 690000, 705000, 1020000, 1035000], color='#e5914b', linewidth="1.0")


plt.legend(['simulation (failure-free)', 'analytic model (failure-free)', 'simulation (failure-prone)', 'analytic model (failure-prone)'], loc='upper left', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processing window ($\mathregular{10^6}$)', fontsize=10)
plt.ylabel('Discards', fontsize=10)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(0, 11, step=1))
plt.yticks(np.arange(0, 1200000, step=200000))


plt.tight_layout()
plt.ylim(0,1200000)



plt.savefig('discards_fails.eps')


