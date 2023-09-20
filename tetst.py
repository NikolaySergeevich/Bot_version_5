import matplotlib.pyplot as plt
import numpy as np

# example data
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# example variable error bar values
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)


# fig, (ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=6, sharex=True,
#                                     figsize=(12, 6))
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained", figsize=(8, 6))
for ax in axs.flat:
    ax.set_axis_off()

axs[0,0].text(0.25, 0.8, 'Программист', size = 13, family='sans-serif', weight='semibold',  horizontalalignment='left')
axs[0,1].text(0.25, 0.8, 'Тестировщик', size = 13, family='sans-serif', weight='heavy',  horizontalalignment='left')
axs[0,2].text(0.25, 0.8, 'Аналитик', size = 13, family='sans-serif', weight='heavy',  horizontalalignment='left')
axs[1,0].text(0.25, 0.8, 'Проджект-\nменеджер', size = 13, family='sans-serif', weight='heavy',  horizontalalignment='left')
axs[1,1].text(0.25, 0.8, 'Продакт-\nменеджер', size = 13, family='sans-serif', weight='heavy',  horizontalalignment='left')

axs[0,0].text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec='#fb7819', fc='#ffffff',))
axs[0,0].text(0.35, 0.43, "4", size=30, weight='roman')
axs[0,0].text(0.6, 0.46, "45", size=30, weight='roman', color = '#fb7819')
axs[0,0].text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = '#fb7819')

axs[0,1].text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec='#fc0fc0', fc='#ffffff',))
axs[0,1].text(0.35, 0.43, "4", size=30, weight='roman')
axs[0,1].text(0.6, 0.46, "45", size=30, weight='roman', color = '#fc0fc0')
axs[0,1].text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = '#fc0fc0')

axs[0,2].text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec='#f5ee00', fc='#ffffff',))
axs[0,2].text(0.35, 0.43, "4", size=30, weight='roman')
axs[0,2].text(0.6, 0.46, "45", size=30, weight='roman', color = '#f5ee00')
axs[0,2].text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = '#f5ee00')

axs[1,0].text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec='#28e4f3', fc='#ffffff',))
axs[1,0].text(0.35, 0.43, "4", size=30, weight='roman')
axs[1,0].text(0.6, 0.46, "45", size=30, weight='roman', color = '#28e4f3')
axs[1,0].text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = '#28e4f3')

axs[1,1].text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec='#9d22f2', fc='#ffffff',))
axs[1,1].text(0.35, 0.43, "4", size=30, weight='roman')
axs[1,1].text(0.6, 0.46, "45", size=30, weight='roman', color = '#9d22f2')
axs[1,1].text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = '#9d22f2')

fig.suptitle('Errorbar subsampling')
plt.show()