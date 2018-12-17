import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])



#[22, 43, 65, 89, 111, 133, 155, 178, 200, 222]
#[19, 22, 16, 16, 17, 17, 4, 18, 18, 19, 17]
plt.plot([1,2,3,4,5,6,7,8,9,10], [27, 55, 77, 105, 133, 160, 189, 216, 244, 266], marker="^", color='#000000')
plt.plot([1,2,3,4,5,6,7,8,9,10], [22, 45, 77, 108, 139, 170, 202, 233, 264, 295], color='#e5914b')
plt.plot([1,2,3,4,5,6,7,8,9,10], [19,19,0,3,5,6,7,8,8,10],  linestyle=':', color='darkslateblue')



#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['simulação', 'modelo analítico', 'erro % simulação'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

#plt.axvline(x=40000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=50000, ymax=1, color='#00b0e7', label='drift')

plt.xlabel('Taxa de processamento de tuplas ($\mathregular{10^5}$)', fontsize=10, fontweight='bold')
plt.ylabel('Latência do sistema (s)', fontsize=10, fontweight='bold')

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1, 11, step=1))
plt.yticks(np.arange(0, 320, step=40))
#plt.xticks(rotation=30)
plt.margins(0)

plt.tight_layout()

#plt.show()
plt.savefig('latencyFail.eps')
