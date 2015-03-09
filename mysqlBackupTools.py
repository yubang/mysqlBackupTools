#coding:UTF-8

"""
mysql备份小脚本
@author:yubang
version:1.0
时间：2015-03-09
"""

import os,time

host="127.0.0.1"
username="root"
password="root"
port="3306"
dirPath="/backup"

def index(db):
    global host,username,password,port,dirPath
    d=time.strftime("%Y%m%d")
    t=time.strftime("%H%M%S")
    path="%s/%s"%(dirPath,d)
    if(not os.path.exists(path)):
        os.makedirs(path)
    #mysqldump -h ip -P 端口 -u 用户名 -p密码 数据库名字 | gzip > 备份目录/当前日期/时间_数据库名字.sql.gz
    command="mysqldump -h %s -P %s -u %s -p%s %s | gzip >  %s/%s/%s_%s.sql.gz"%(host,port,username,password,db,dirPath,d,t,db)
    os.system(command)
    print command
    
if __name__ == "__main__":
    index("blog")
