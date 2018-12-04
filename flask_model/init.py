from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from main.app  import app
from main.db_operate import db
from main.settings  import *


#构建制定操作
manage=Manager(app)
#构建数据库迁移
migrate=Migrate(app,db)
#添加数据库迁移指令
manage.add_command('db',MigrateCommand)


if  __name__ == "__main__":
    manage.run()