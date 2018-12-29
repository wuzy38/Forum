import pymysql
import datetime

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
            data = conn.select_from("plate")
            print(str((1, 2)))
            conn.insert_into('plate', ('4', '中国'))
            print(conn.select_from('plate'))
            print(str(("1'2'", '3', 123)))
            conn.delete_from('plate', 'where plate_id=4')
            print(conn.select_from('plate'))

            print(conn.update('plate', "plate_name='美国'", 'where plate_id=3'))
            print(conn.select_from('plate'))
            conn.insert_into('plate', ('1', 'NULL'))

            print(conn.select_from('plate'))

            conn.insert_into('user', (1, '徐立', '1997-12-21 19:00:01', 0, '519', '519519519'))
            print(conn.select_from('user'))
            print(conn.check_user(519))

    finally:
        conn.close()


def generate_data():
    s = sql()

    s.insert_into('plate', ('1', '中山大学', 0))
    s.insert_into('plate', ('2', '数据库', 0))
    table_name = 'user'
    for i in range(9):
        s.insert_into(table_name, (i, 'name'+str(i), '2018-12-29 00:05:03', i, 'acount'+str(i), 'password'+str(i)))

    table_name = 'theme'
    for i in range(9):
        s.insert_into(table_name, (i, '主题'+str(i), '2018-12-29 00:05:03', 1, str(i)))

    s.create_user('acount999', 'password999', 'user_name999')



class sql():
    def __init__(self):
        self.conn = pymysql.connect(host="172.18.35.138", user="wuzy", password="519519519", db="forum")
        # self.conn = pymysql.connect(host="localhost", user="root", password="88720073", db="forum")

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

    def check_user(self, user_account):
        """检查用户是否在user表中"""
        data = self.select_from('user', '*', 'where user_account='+str(user_account))
        if len(data) > 0:
            return True
        return False

    def get_user_info(self, user_name):
        """获取用户的信息的字典，依次为id, name, register_time, grade, user_account"""
        data = self.select_from('user', '*', 'where user_name='+str(user_name))
        dic = {}
        if len(data > 0):
            dic['id'] = data[0]
            dic['name'] = data[1]
            dic['register_time'] = data[2]
            dic['grade'] = data[3]
            dic['user_account'] = data[4]
        return dic

    def get_linked_num(self, id):
        """获取被关注的数目"""
        data = self.select_from('link', '*', 'where user_linked_id='+str(id))
        return len(data)

    def get_all_theme(self, plate_id):
        """返回一个版块所有的主题dict的list，依次顺序为theme_id, theme_name, theme_time, plate_id, user_id"""
        data = self.select_from('theme', '*', 'where plate_id='+str(plate_id))
        res = []
        for i in range(len(data)):
            tmp_dict = {'theme_id':data[i][0],
                        'theme_name':data[i][1],
                        'theme_time':data[i][2],
                        'plate_id':data[i][3],
                        'user_id':data[i][4]}
            res.append(tmp_dict)
        return res

    def create_user(self, account, password, user_name):
        """创建用户，输入账号、密码、用户名即可"""
        data = self.select_from('user')
        num = len(data)
        time_str = self.get_time()
        return self.insert_into('user', (num, user_name, time_str, 0, account, password))

    def get_reply(self, theme_id):
        """获取指定theme_id下的所有回复，为字典的list，依次属性为reply_id, user_id, content, reply_time, theme_id"""
        data = self.select_from('reply', '*', 'where theme_id='+str(theme_id))
        res = []
        for i in range(len(data)):
            tmp_dic = {'reply_id':data[0],
                       'user_id':data[1],
                       'content':data[2],
                       'reply_time':data[3],
                       'theme_id':data[4]}
            res.append(tmp_dic)
        return res

    def do_reply(self, user_id, content, theme_id):
        """回复一个主题，传入用户id，内容，主题号"""
        data = self.select_from('reply')
        reply_id = len(data)
        datetime_str = self.get_time()
        return self.insert_into('reply', (reply_id, user_id, content, datetime, theme_id))


    def get_time(self):
        """获取当前时间格式"""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


generate_data()
sql_p = sql()