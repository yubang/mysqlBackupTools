# coding:UTF-8


"""
备份管理器
@author: yubang
创建于2018年8月8日
"""


from config import config
from lib import system_log_client
from datetime import datetime
import os
import shutil


class BackupManagerService:

    def __init__(self):
        self.n = int(datetime.now().strftime("%Y%m%d"))

    def gc(self):
        """删除过期的备份"""
        if config.backup_max_retain_day <= 0:
            # 不删除备份
            return

        fps = os.listdir(os.path.dirname(config.backup_path))
        for fp in fps:
            path = os.path.join(config.backup_path, fp)
            if not os.path.isdir(path):
                continue
            if self.is_need_delete(fp):
                # 删除备份
                system_log_client.info("删除备份："+path)
                shutil.rmtree(path)

    def is_need_delete(self, file_name):
        """判断是否需要删除"""
        try:
            n = int(file_name)
        except ValueError:
            return False

        return self.n - n > config.backup_max_retain_day

