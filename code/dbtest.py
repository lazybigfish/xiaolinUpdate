import sqlite3

conn = sqlite3.connect('test.db')
print('open db success!')

c = conn.cursor()
# sql = "create table one (fundcode varchar(20) primary key,name varchar(30));"
# sql = " insert into one(fundcode,name) values(\'008990\',\'这个是基金\')"
# sql = "select * from one"
c.execute(sql)
values = c.fetchall()
print(values)