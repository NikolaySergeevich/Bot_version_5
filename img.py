import data_frame as wor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import os
import text as t
from sqlyghter import Sqloghter


#инициализирукм соединение с БД
db = Sqloghter()


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
    sum_bals = wor.get_sum_data(df)

    db.update_degry_whis_dinamic_reqest(us_id, 'sum_general_bals', sum_bals)#обновляет общую сумму балов в БД
    db.connection.commit()
    db.commit()

    plt.text(-1, -1, sum_bals, size = 40, horizontalalignment='center',
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
    for rr, bar in zip(r, bars):
        if rr == 1: color = '#505160' 
        if rr == 2: color = '#6a71' 
        if rr == 3: color = '#68829e' 
        if rr == 4: color = '#aebd38' 
        if rr == 5: color = '#598234' 
        bar.set_facecolor(color)
        # bar.set_height(0) #изменяет высоту бара
    # plt.show()
    way = t.get_way_of_img(us_id)#путь и название для картинки
    plt.savefig(way)


def create_5_pl(us_id, arr_name_spec):
    N = 15
    df = wor.get_data_frame(us_id) #тут получим словарь
    r = np.array(wor.get_data_frame_only_value(df))#список только со значениями
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = np.array([0.42] * N)
    title2 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    color = '#500805'

    lable = t.get_list_whis_title_on_russian()
    
    for name, name_compare in zip(arr_name_spec, t.name_compsre_specific):
        plt.figure(figsize=(12,10), facecolor='#f9f9ff')#фон окна. Цвет - хлопок
        ax = plt.subplot(111, polar=True)

        # plt.text(-1, -1, wor.get_sum_data(df), size = 40, horizontalalignment='center',
        #     verticalalignment='center', color = color)#делает в центре надпись суммы очков
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
        df_const = wor.get_data_frame(name)
        df_per = wor.get_data_frame(us_id)
        r_cons = np.array(wor.get_data_frame_only_value(df_const))
        r_per = np.array(wor.get_data_frame_only_value(df_per))
        bar_cons = ax.bar(x=theta, height=r_cons-.0, width=width, bottom=0, alpha=0.7, tick_label=title2, align='edge', color = color)
        
        color_green = '#2e8b57'#зелёный
        color_red = '#cc0605'#красный
        color_wite = '#ffffff'#белый
        bals = 0
        for r_p, r_cons, bar, bar_cons in zip (r_per, r_cons, bars, bar_cons):
            bar.set_facecolor(color_wite)
            bar_cons.set_facecolor(color_wite)
            if r_p > r_cons and r_cons > 0:
                bar_cons.set_facecolor(color_red)
                bar.set_facecolor(color_green)
                bals += r_p
            if r_p == r_cons:
                bar_cons.set_facecolor(color_green)
                bar.set_facecolor(color_wite)
                bals += r_p
            if r_p < r_cons:
                bar_cons.set_facecolor(color_red)
                bar.set_facecolor(color_green)
            if r_cons == 0:
                bar.set_facecolor(color_red)
        plt.text(-1, -1, bals, size = 40, horizontalalignment='center',
            verticalalignment='center', color = color)
        db.update_degry_whis_dinamic_reqest(us_id, name_compare, bals)#ОБНОВЛЯЕМ данные в базе данных. Кол-во балов набраных при сравнении со специальностью
        db.connection.commit()
        db.commit()
        
        way = t.get_way_of_img_compare(us_id, name)#путь и название для картинки
        plt.savefig(way)

def img_with_resalt(us_id, user_name): #этот метод создаёт итоговую картинку
    fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained", figsize=(8, 6), facecolor='#f9f9ff')
    for ax, name, colo, name_compare in zip(axs.flat, t.name_specific_rus, t.color_for_finish_img, t.name_compsre_specific):
        ax.text(0.25, 0.8, name, size = 13, family='sans-serif', weight='semibold',  horizontalalignment='left')
        ax.text(0.3, 0.45, "      ", size=25, bbox=dict(boxstyle="round", ec=colo, fc='#f9f9ff'))
        ax.text(0.6, 0.385, "Проходной\nбал", size=6, weight='roman', color = colo)
        ax.text(0.35, 0.43, db.giv_volue_compare(name_compare, us_id), size=30, weight='roman')
        ax.text(0.6, 0.46, t.defolt_resulr_passing_grade[name], size=30, weight='roman', color = colo)
    for ax in axs.flat:
        ax.set_axis_off()

    fig.suptitle('Твой результат, ' + user_name, verticalalignment='top', weight='semibold')
    way = t.get_way_of_finish_img(us_id)#путь и название для картинки
    plt.savefig(way)
    db.update_link_finish_img(us_id)
    db.connection.commit()
    db.commit()
    # plt.show()

def remove_img(name_img): 
    path = name_img
    try:
        os.remove(path)
    except:
        print('Изображение отсутствует')