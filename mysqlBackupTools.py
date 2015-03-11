#coding:UTF-8

"""
mysql备份小脚本
@author:yubang
version:1.0
时间：2015-03-09
"""

import os,time,datetime

#数据库ip或者域名
host="127.0.0.1"
#数据库用户名
username="root"
#数据库密码
password="root"
#数据库端口
port="3306"
#备份目录
dirPath="/backup"
#数据库备份保留天数
maxBackupDays=1
#在备份后删除过期备份，False则在备份前删除过期备份
deleteAfterBackup=True

def deleteDir(path):
    "递归删除文件和文件夹"
    if(os.path.exists(path)):
        if(os.path.isdir(path)):
            fps=os.listdir(path)
            for fp in fps:
                deleteDir(path+"/"+fp)
            os.rmdir(path)
        else:
            os.remove(path)

def deleteTooManyBackup():
    "删除过多的备份"
    global maxBackupDays,dirPath
    obj=datetime.datetime.now()-datetime.timedelta(days=maxBackupDays-1)
    title=obj.strftime("%Y%m%d")
    fps=os.listdir(dirPath)
    for temp in fps:
        if(int(temp)<int(title)):
            #删除该备份
            deleteDir(dirPath+"/"+temp)
    
def index(db,d,t):
    "利用mysqldump备份数据库"
    global host,username,password,port,dirPath
    #mysqldump -h ip -P 端口 -u 用户名 -p密码 数据库名字 | gzip > 备份目录/当前日期/时间_数据库名字.sql.gz
    command="mysqldump -h %s -P %s -u %s -p%s %s | gzip >  %s/%s/%s_%s.sql.gz"%(host,port,username,password,db,dirPath,d,t,db)
    os.system(command)
    print command

def init(dbList):
    "入口函数"
    global deleteAfterBackup,dirPath
    
    d=time.strftime("%Y%m%d")
    t=time.strftime("%H%M%S")
    path="%s/%s"%(dirPath,d)
    if(not os.path.exists(path)):
        os.makedirs(path)
    
    if(not deleteAfterBackup):
        deleteTooManyBackup()
    for dbName in dbList:
        index(dbName,d,t)
    if(deleteAfterBackup):
        deleteTooManyBackup()
        
if __name__ == "__main__":
    init(['blog'])
