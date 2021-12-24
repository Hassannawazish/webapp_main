import os
print('saasas')
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = "postgres"
pwd = "myPassword"
db = "3dprint"
host = "localhost"
port = "5432"
db_url = 'postgresql://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
def init_db():
    from application.models import login_manager
    Base.metadata.create_all(bind=engine)