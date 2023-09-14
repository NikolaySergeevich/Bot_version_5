import data_frame as wor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import os
import text as t



def plt_result(us_id):
    N = 15
    df = wor.get_data_frame(us_id) #тут получим словарь
    r = np.array(wor.get_data_frame_only_value(df))#список только со значениями
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = np.array([0.42] * N)
    title2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    color = '#500805'

    lable = t.get_list_whis_title_on_russian()
    plt.figure(figsize=(12,10), facecolor='#f9f9ff')#фон окна. Цвет - хлопок
    ax = plt.subplot(111, polar=True)

    plt.text(-1, -1, wor.get_sum_data(df), size = 40, horizontalalignment='center',
        verticalalignment='center', color = color)#делает в центре надпись суммы очков
    # --------------------Заполнение окружности по уровням 
    ycoord = 0.45
    for num in 1,2,3,4,5:
        xcoord = 0.20943951
        ygol = -85
        i = 0
        while i != N:
            plt.text(xcoord, ycoord, num, rotation=ygol, size=13, horizontalalignment='center', verticalalignment='center', alpha=0.5)
            xcoord += 0.41887902
            ygol += 24.8
            i += 1
        ycoord +=1
        
    #------------заполнение качеств по окружности
    ycoord = 0.20943951
    for lab in lable:
        xcoord = 6.3
        plt.text(ycoord, xcoord, lab, size=9, horizontalalignment='center', verticalalignment='center', weight='medium', family='serif')
        ycoord += 0.41887902

    ax.set_rlim(0)
    ax.set_rticks(np.arange(1, 6, 1))
    ax.set_rorigin(-1)
    ax.set_thetagrids(theta * 180 / np.pi, title2)
    ax.yaxis.set_major_formatter(NullFormatter())
    ax.grid(color ="black", linewidth=3)


    bars = ax.bar(x=theta, height=r-.0, width=width, bottom=0, alpha=0.7, tick_label=title2, align='edge', color = color)
    # name_specific = ["analist", "tester", "developer", "prodact", "project"]
    color_list = []
    
    if us_id == "analist":
        color_list = t.color_for_analist
        print(color_list)
    if us_id == "tester":
        color_list = t.color_for_tester
        print(color_list)
    if us_id == "developer":
        color_list = t.color_for_developer
        print(color_list)
    if us_id == "prodact":
        color_list = t.color_for_prodact
        print(color_list)
    if us_id == "project":
        color_list = t.color_for_project
        print(color_list)
    

    for rr, bar in zip(r, bars):
        if rr == 1: color = color_list[0] 
        if rr == 2: color = color_list[1] 
        if rr == 3: color = color_list[2] 
        if rr == 4: color = color_list[3] 
        if rr == 5: color = color_list[4] 
        bar.set_facecolor(color)
    way = t.get_way_of_img(us_id)#путь и название для картинки
    plt.savefig(way)




for i in t.name_specific:
    plt_result(i)