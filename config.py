# coding:UTF-8

from datetime import datetime
import configparser
import os


class Config:
    def __init__(self):
        config_parser = configparser.ConfigParser()
        conf_dir = os.path.join(os.path.dirname(os.path.realpath(__name__)), "conf")
        config_file_path = os.path.join(conf_dir, "default.conf")
        config_parser.read(config_file_path)

        # 读取配置文件的数据
        self.system_log_level = config_parser.get('system','log_level')
        self.system_log_path = config_parser.get("system", "log_path")

        self.mysql_db_list = [] if config_parser.get("mysql", "db") == "" else config_parser.get("mysql", "db").split(",")
        self.mysql_backup_all_db = config_parser.get("mysql", "all_db") == 'true'
        self.mysql_username = config_parser.get("mysql", "user")
        self.mysql_password = config_parser.get("mysql", "password")
        self.mysql_host = config_parser.get("mysql", "host")
        self.mysql_port = int(config_parser.get("mysql", "port"))

        self.backup_path = config_parser.get("backup", "path") + datetime.now().strftime("%Y%m%d") + "/%s-" + datetime.now().strftime("%Y%m%d%H%M%S") + ".sql"

    def init(self):
        """初始化程序必要数据"""
        if not os.path.exists(self.system_log_path):
            os.makedirs(self.system_log_path)


config = Config()
config.init()
