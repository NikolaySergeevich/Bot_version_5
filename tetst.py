import matplotlib.pyplot as plt
import text as t
from sqlyghter import Sqloghter


#инициализирукм соединение с БД
db = Sqloghter()

fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained", figsize=(8, 6))
for ax, name, colo, name_compare in zip(axs.flat, t.name_specific_rus, t.color_for_finish_img, t.name_compsre_specific):
        ax.text(0.25, 0.8, name, size = 13, family='sans-serif', weight='semibold',  horizontalalignment='left')
        ax.text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec=colo, fc='#ffffff'))
        ax.text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = colo)
        ax.text(0.35, 0.43, db.giv_volue_compare(name_compare, '843471050'), size=30, weight='roman')
        ax.text(0.6, 0.46, t.defolt_resulr_passing_grade[name], size=30, weight='roman', color = colo)
for ax in axs.flat:
        ax.set_axis_off()

fig.suptitle('Errorbar subsampling' + 'sdfsdg', verticalalignment='top', weight='semibold')
plt.show()