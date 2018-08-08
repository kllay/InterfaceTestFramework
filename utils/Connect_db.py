#coding:utf-8
import pymysql
from utils.FileUtils import FileUtils

class ConnectDb:
    def create_init(self,host,port,user,password,dbname):
        # 打开数据库连接
        #self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
        self.conn = pymysql.connect(host=host, port=int(port), user=user, passwd=password, db=dbname)
        # 创建游标
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_data_one(self,sql):
        try:
            print(sql)
            self.cursor.execute(sql)
            #col=self.cursor.description
            result=self.cursor.fetchone()
            return result
        except:
            print("数据库语句不对！")
            return  None

    def get_sms_db(self):
        filepath = "../../zhanghao/sqldb.txt"
        file=FileUtils()
        lists=file.get_file_value(filepath)
        print(lists)
        self.create_init(lists[0],lists[1],lists[2],lists[3],lists[4],)






if __name__=="__main__":
    con=ConnectDb()
    sql='select * from login'
    result=con.get_data_one(sql)
    print(result)


    '''
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
    # 创建游标
    cursor = conn.cursor()
    #执行sql语句
    cursor.execute('select * from ly ')
    result = cursor.fetchone()
    # 获取第一行数据
    #row_1 = cursor.fetchone()
    # 获取前n行数据
    # row_2 = cursor.fetchmany(3)
    # 获取所有数据
    # row_3 = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    print(result)
    '''















