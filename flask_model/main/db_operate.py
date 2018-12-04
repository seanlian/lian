from .app import app
from flask_sqlalchemy import SQLAlchemy
from .settings import DATABASE




app.config['SQLALCHEMY_DATABASE_URI']='{database}+{driver}://{user}:{password}@{host}/{db}'.format(**DATABASE)


db=SQLAlchemy(app)

class DBO():
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
    @classmethod
    def add(self,*args,**kwargs):
        if len(args)>0 and isinstance(*args,list):
            for dic in args[0]:
                obj=self(**dic)
                db.session.add(obj)
        else:
            obj=self(**kwargs)
            db.session.add(obj)
        db.session.commit()

    def update(self,**kwargs):
        for key,value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key,value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
