#TODO 크롤링한 데이터에 대한 후처리. 예를 들면 필터링이라든지, 혹은 파일 Export, DB 처리 등...

import pymysql

def connectDatabase():
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='test_db', charset='utf8')
    return conn

def selectDatabase(connect):
    curs = connect.cursor()
    curs.execute('select * from user')
    data = curs.fetchall()
    print(data)

def insertDatabase(connect):
    curs = connect.cursor()
    curs.execute('insert into user values')

    #TODO exception 처리에 따라 db.commit, 혹은 db.rollback을 해야 한다...
