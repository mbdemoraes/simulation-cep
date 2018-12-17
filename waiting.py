import matplotlib.pyplot as plt
import numpy as np


N = 4
men_means = (20, 35, 30, 35)
men_std = (2, 3, 4, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.20       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r')

women_means = (25, 32, 34, 20)
women_std = (3, 5, 2, 3)
rects2 = ax.bar(ind + width, women_means, width, color='b')

teste_means = (30, 32, 30, 15)
teste_std = (3, 5, 2, 3)
rects3 = ax.bar(ind + width*2, teste_means, width, color='g')



# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Operator 1', 'Operator 2', 'Operator 3', 'Operator 4'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Men', 'Women', 'Case 3'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/3., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


plt.savefig('waiting.eps')
