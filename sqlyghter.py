import pymysql
from config import userr, passwordd, hostt, db_namee
import text as t

class Sqloghter:
    def __init__(self):
        self.connection = pymysql.connect(
            user=userr,
            host=hostt,
            port=3306,
            password=passwordd,
            database=db_namee,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

# ===================================================================
# применение процедуры
    def check_exists_user(self, user_id):
        # добавляет пользователя в 2 таблицы, если его там ещё нет и возвращает есть он там или нет.
        self.cursor.execute("CALL check_exists_user ('{0}');".format(user_id))
        list = self.cursor.fetchall()
        item = list[0]['item']
        return item

    def add_user_in_users(self, user_id):
        # добавляет пользователя в 2 таблицы, если его там ещё нет и возвращает есть он там или нет.
        return self.cursor.execute("CALL AddUser ('{0}');".format(user_id))
    
    def add_user_in_cat(self, user_id):
        # добавляет пользователя в 2 таблицы, если его там ещё нет и возвращает есть он там или нет.
        return self.cursor.execute("CALL AddUserincat ('{0}');".format(user_id))
    
    def check_passed_the_test(self, user_id):
        # вызывает процедуру, которая возвращает знчение indicate пользователя
        self.cursor.execute("CALL check_passed_the_test ('{0}')".format(user_id))
        list = self.cursor.fetchall() #это команда возвращает список в котором лежит словарь {'indicate': 0}
        item = list[0]['indicate'] # получаем значение из словаря по ключу 'indicate'
        return item
    
    def get_value_capabilities(self, user_id):
        '''получаем данные из таблицы  capabilities по user_id'''
        self.cursor.execute("CALL get_value_capabilities ('{0}')".format(user_id))
        list = self.cursor.fetchall() #это команда возвращает список в котором лежит словарь
        return list
    
    def update_user(self, user_id, indicate):
        # изменяет поле indicate у пользователя
        return self.cursor.execute("CALL update_indicate_user ('{0}', {1})".format(user_id, indicate))
    
    def update_time_content_test(self, user_id):
        return self.cursor.execute("CALL update_time_content_test ('{0}')".format(user_id))
    
    def update_degry(self, user_id, column_name, degry):
        #использовние 15 разных процедур. Каждая для отдельного столбца
        procedure_name = 'update_degry_' + column_name
        return self.cursor.execute("CALL {0} ('{1}', {2});".format(procedure_name, user_id, degry))
    
    def update_degry_whis_dinamic_reqest(self, user_id, column_name, degry):
        #применение одной процедуры с использованием динамического запроса
        return self.cursor.execute("CALL update_degry ('{0}', '{1}', '{2}')".format(column_name, user_id, degry))
    
    def update_link_data_test(self, user_id):
        #записываем ссылку картинки в базу 
        return self.cursor.execute("CALL update_link_data_test ('{0}', '{1}')".format(user_id, t.get_way_of_img(user_id)))
                
    def update_link_copmare(self, user_id, name_specific):
        #использовние 5 разных процедур. Каждая для отдельного графика сравнения
        procedure_name = 'update_link_data_compare_' + name_specific
        return self.cursor.execute("CALL {0} ('{1}', '{2}');".format(procedure_name, user_id, t.get_way_of_img_compare(user_id, name_specific)))
    
    



# =================================================================== 

    def get_users(self, indicate = 1):
        """Получаем всех активных подписчиков бота"""
        # with self.connection:
        return self.cursor.execute("SELECT * FROM `users` WHERE `indicate` = '{0}'".format(indicate)).fetchall()
    
        
    def commit(self):
        """Вносим изменение в табл"""
        self.connection.commit()
    
    def close(self):
        """Закрываем соединение с бд"""
        self.connection.close()


            