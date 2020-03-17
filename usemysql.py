#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "d", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
#cursor.execute("SELECT * from employee;")

# 使用 fetchone() 方法获取一条数据
#data = cursor.fetchone()

#print "Database version : %s " % data

# SQL 查询语句
sql = "SELECT * FROM employee;"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      eid = row[0]
      name = row[1]
      age = row[2]
      income = row[3]
      # 打印结果
      print (eid, name, age, income)
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
