# mysql备份小工具
* * * * *

## 平台环境要求：
* python3.6+
* 支持mysqldump和mysql，gzip命令

## 快速开始：
* git clone git@github.com:yubang/mysqlBackupTools.git
* 修改conf/default.conf
* 配置定时任务，定时执行python3 backup.py

## conf/default.conf配置说明

```
[system]
# 日志等级，可以选择DEBUG，INFO，WARN
log_level = DEBUG
# 日志存储目录
log_path = ./log

[mysql]
# 要备份的mysql地址
host = 127.0.0.1
# 要备份的mysql端口
port = 3306
# 要备份的mysql用户名
user = root
# 要备份的mysql密码
password = root
# 要备份的mysql的数据库列表，逗号隔开
db = blog
# 是否备份所有数据库，true，false，如果为true则上面db参数失效
all_db = true

[backup]
# 备份目录地址
path = d:/abc/123
# 备份保留天数
max_retain_day = 30
# 是否启用gzip压缩
gzip = true
```

## 注意：

* 本工具忽略备份information_schema和performance_schema
* 备份请自行校验是否正确

