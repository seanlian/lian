from .app import app
from hand.views import *
from hand.settings import hand
from floder.settings import fl
from floder.views import *
#注册蓝图
BLUE_PRINTS=[
app.register_blueprint(hand, url_prefix="/hand/"),
app.register_blueprint(fl, url_prefix="/fl/"),

]


#配置数据库信息
DATABASE={
    'database':'mysql',
    'driver':'pymysql',
    'user':'root',
    'password':'123',
    'host':'127.0.0.1',
    'db':'test'
}

