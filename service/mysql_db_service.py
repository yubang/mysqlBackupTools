# coding:UTF-8


"""
获取需要备份的mysql的数据库列表
@author: yubang
"""

from config import config
from service.mysql_option_service import MysqlOptionService


class MysqlDbManage:
    def get_db_list(self): pass


class AllMysqlDbManager(MysqlDbManage):
    def get_db_list(self):
        return MysqlOptionService().get_db_list()


class AppointMysqlDbManager(MysqlDbManage):
    def get_db_list(self):
        return config.mysql_db_list
