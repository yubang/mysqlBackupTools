# coding:UTF-8


"""
数据库操作封装
@author: yubang
创建于2018年8月7日
"""

from config import config
from lib import system_log_client
import os


class MysqlOptionService:
    def get_db_list(self):
        """获取数据库列表"""
        cmd = "mysql -u %(username)s -p%(password)s -P %(port)d -h %(host)s -e 'show databases;'" % {
            "username": config.mysql_username,
            "password": config.mysql_password,
            "port": config.mysql_port,
            "host": config.mysql_host,
        }
        s = os.popen(cmd).read()
        arrs = s.split("\n")
        return [obj for index, obj in enumerate(arrs) if index != 0 and obj and obj != 'information_schema']

    def backup_db(self, db):
        """备份数据库"""
        target_file_path = config.backup_path % db
        target_file_dir_path = os.path.dirname(target_file_path)
        cmd = "mysqldump -u %(username)s -p%(password)s -P %(port)d -h %(host)s %(db)s > %(path)s " % {
            "username": config.mysql_username,
            "password": config.mysql_password,
            "port": config.mysql_port,
            "host": config.mysql_host,
            "path": target_file_path,
            "db": db
        }

        # 预先创建数据库存储目录
        if not os.path.exists(target_file_dir_path):
            os.makedirs(target_file_dir_path)

        # 执行命令
        system_log_client.debug("执行命令："+cmd)
        os.system(cmd)
