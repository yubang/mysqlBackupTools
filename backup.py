# coding:UTF-8


from lib import system_log_client
from config import config
from service.mysql_db_service import AllMysqlDbManager, AppointMysqlDbManager
from service.mysql_option_service import MysqlOptionService


# 获取要备份的db列表
if config.mysql_backup_all_db:
    db_list = AllMysqlDbManager().get_db_list()
else:
    db_list = AppointMysqlDbManager().get_db_list()

for db in db_list:
    system_log_client.info("开始备份数据库："+db)
    MysqlOptionService().backup_db(db)