import pandas as pd
from sqlyghter import Sqloghter
import text as t

db = Sqloghter()


# метод получения словаря с 15 ключами и значениями к ним из таблицы capabilities
def get_data_frame(user_id):
    data = db.get_value_capabilities(user_id)[0]
    data.pop('id')
    data.pop('user_id')
    return data

# метод получения суммы очков, которая считается из результатов прохождения теста
def get_sum_data(data):
    res = 0
    for i in t.get_list_whis_title_on_english():
        res = res + data[i]
    return res

# метод получения списка с результатами теста
def get_data_frame_only_value(data):
    list = []
    for i in t.get_list_whis_title_on_english():
        list.append(data[i])
    return list
