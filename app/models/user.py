import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///shop.db', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('first_name', String),
                    Column('last_name', String),
                    Column('email', String),
                    Column('password', String)
                    )

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.first_name, self.last_name, self.email, self.password)


# Создание таблицы
Base.metadata.create_all(engine)
