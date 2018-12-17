import matplotlib.pyplot as plt
import numpy as np


y = np.arange(1,11,1)


plt.subplot(211)
plt.plot(y, [337680, 584992],  marker="^", color='#000000')
plt.plot(y, [555000],  color='#e5914b')


plt.legend(['simulation', 'analytic model'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

plt.xlabel('Processing window ($\mathregular{10^6}$)', fontsize=12)
plt.ylabel('Unprocessed tuples', fontsize=12)

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1, 11, step=1), size=12)
plt.yticks(np.arange(0, 800000, step=200000), size=12)
plt.margins(0)

plt.tight_layout()

