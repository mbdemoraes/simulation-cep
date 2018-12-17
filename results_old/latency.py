import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(10)
x = np.arange(500)

#plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])


#[4545, 4651, 4615, 4494, 4504, 4511, 4516, 4494, 4500, 4504]

#fail [22, 55, 94, 116, 144, 194, 222, 250, 272, 323]
#nfail [22, 43, 65, 89, 111, 133, 155, 178, 200, 222]
#diferenca [0, 12, 29, 27, 33, 61, 67, 72, 72, 101]

plt.plot([1,2,3,4,5,6,7,8,9,10], [22, 43, 65, 89, 111, 133, 155, 178, 200, 222], marker="^", color='#000000')
plt.plot([1,2,3,4,5,6,7,8,9,10], [20.9, 42.9, 64.9, 86.9, 108.9, 130, 152, 174.9, 196.9, 218.9],  color='#e5914b')
plt.plot([1,2,3,4,5,6,7,8,9,10], [5,0.1,0.1, 2.4, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0],  linestyle=':', color='#000000')


#plt.legend(['NB', 'y = 2x', 'y = 3x', 'y = 4x'], loc='upper left')
plt.legend(['simulação', 'modelo analítico', 'erro % simulação'], loc='‘lower right', fontsize='small', shadow=True, fancybox=True)

#plt.axvline(x=40000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=60000, ymax=1, color='#00b0e7', ls='--', linewidth=2)
#plt.axvline(x=50000, ymax=1, color='#00b0e7', label='drift')

plt.xlabel('Taxa de processamento de tuplas ($\mathregular{10^5}$)', fontsize=10, fontweight='bold')
plt.ylabel('Latência do sistema (s)', fontsize=10, fontweight='bold')

plt.grid(color='0.75', linestyle='-.', linewidth=0.3)
plt.xticks(np.arange(1, 11, step=1))
plt.yticks(np.arange(0, 240, step=40))
#plt.xticks(rotation=30)
plt.margins(0)

plt.tight_layout()

#plt.show()
plt.savefig('latency.eps')
