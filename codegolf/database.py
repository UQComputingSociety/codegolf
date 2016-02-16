import sqlalchemy as sa
import sqlalchemy.orm as sao
from . import app
import codegolf
from sqlalchemy.ext.declarative import declarative_base

engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                          convert_unicode=True)

db_session = sao.scoped_session(sao.sessionmaker(bind=engine))
Base = codegolf.Base()
Base.query = db_session.query_property()


def init_db():
    import codegolf.models
    Base.metadata.create_all(bind=engine)