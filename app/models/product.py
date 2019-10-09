import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, REAL
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///shop.db', echo=True)


# Создание таблицы
Base.metadata.create_all(engine)
