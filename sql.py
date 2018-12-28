import pymysql

def test():
    conn = pymysql.connect(host="localhost", user="root", password="88720073", db="forum")
    try:
        with conn.cursor() as cursor:
            # sql = "SELECT * FROM plate;"
            sql = "INSERT INTO plate VALUES(2,'中山大学')"
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            conn.commit()

    finally:
        conn.close()

class sql():
    def __init__(self):
        #conn = pymysql.connect(host="localhost", user="wuzy", password="519519519", db="forum")
        self.conn = pymysql.connect(host="localhost", user="root", password="88720073", db="forum")

    def __del__(self):
        self.conn.close()

    def select_from(self, table_name, attribute='*', predicate=''):
        """获得table_name信息,返回元组，失败返回None"""
        with self.conn.cursor() as cursor:
            sql_lang = "SELECT " + attribute + "FROM " + table_name + ' ' + predicate
            try:
                cursor.execute(sql_lang)
                self.conn.commit()
                data = cursor.fetchall()
            except Exception as e:
                print('SELECT FAILED!\n Error message:', str(e))
                self.conn.rollback()
                return None
        return data

    def insert_into(self, table_name, tuple):
        """插入表信息，成功返回True，失败返回False"""
        with self.conn.cursor() as cursor:
            sql_lang = "INSERT INTO " + table_name + " VALUES " + str(tuple)
            try:
                cursor.execute(sql_lang)
                self.conn.commit()
            except Exception as e:
                print('INSERT FAILED!\n Error message:', str(e))
                self.conn.rollback()
                return False
        return True

    def delete_from(self, table_name, predicate=''):
        """获得table_name信息,成功返回True,失败返回False"""
        with self.conn.cursor() as cursor:
            sql_lang = "DELETE FROM " + table_name + ' ' + predicate
            try:
                cursor.execute(sql_lang)
                self.conn.commit()
            except Exception as e:
                print('DELETE FAILED!\n Error message:', str(e))
                self.conn.rollback()
                return False
        return True

    def update(self, table_name, attribute, predicate=''):
        """更新表的内容，成功返回True，失败返回False"""
        with self.conn.cursor() as cursor:
            sql_lang = "UPDATE " + table_name + ' SET ' + attribute + ' ' + str(predicate)
            try:
                cursor.execute(sql_lang)
                self.conn.commit()
            except Exception as e:
                print('UPDATE FAILED!\n Error message:', str(e))
                self.conn.rollback()
                return False
        return True

    def check_user(self, user_name):
        """检查用户是否在user表中"""
        data = self.select_from('user', '*', 'where user_account='+str(user_name))
        if len(data) > 0:
            return True
        return False


sql_p = sql()
data = sql_p.select_from("plate")
print(str((1,2)))
sql_p.insert_into('plate', ('4', '中国'))
print(sql_p.select_from('plate'))
print(str(("1'2'",'3',123)))
sql_p.delete_from('plate', 'where plate_id=4')
print(sql_p.select_from('plate'))

print(sql_p.update('plate', "plate_name='美国'", 'where plate_id=3'))
print(sql_p.select_from('plate'))
sql_p.insert_into('plate', ('1', 'NULL'))

print(sql_p.select_from('plate'))

sql_p.insert_into('user', (1, '徐立', '1997-12-21 19:00:01', 0, '519', '519519519'))
print(sql_p.select_from('user'))
print(sql_p.check_user(518))