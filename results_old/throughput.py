import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.gca().set_color_cycle(['blue'])

#[27, 55, 77, 105, 133, 160, 189, 216, 244, 266]
plt.plot([1,2,3,4,5,6,7,8,9,10], [4545, 4651, 4615, 4494, 4504, 4511, 4516, 4494, 4500, 4504], marker="o", color='black')
plt.plot([1,2,3,4,5,6,7,8,9,10], [3703,3636, 3896, 3809,3759, 3750, 3703, 3703, 3688 , 3759], marker="d", color='orangered')
#[842, 1015, 719, 685, 745, 761, 813, 791, 812, 745]


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['Caso 1', 'Caso 2'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

#plt.axvline(x=40000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=50000, ymax=1, color='#00b0e7', label='drift')

plt.xlabel('Taxa de processamento de tuplas ($\mathregular{10^5}$)', fontsize=10, fontweight='bold')
plt.ylabel('Throughput (tuplas/s)', fontsize=10, fontweight='bold')

plt.grid(color='0.75', linestyle='-.', linewidth=0.1)
plt.xticks(np.arange(1, 11, step=1))
plt.yticks(np.arange(1000, 6500, step=500))
#plt.xticks(rotation=30)
#plt.margins(0)

plt.tight_layout()

#plt.show()
plt.savefig('throughput.eps')
