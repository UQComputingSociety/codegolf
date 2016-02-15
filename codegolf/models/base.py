from sqlalchemy.ext.declarative import declarative_base, declared_attr

__all__ = ["Base"]


class ORMAncestor(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=ORMAncestor)
